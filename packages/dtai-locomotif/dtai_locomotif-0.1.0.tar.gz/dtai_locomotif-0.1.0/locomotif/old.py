def _calculate_fitnesses(start_mask, end_mask, mask, n, paths, l_min, l_max, allowed_overlap=0, pruning=True):
    ss = np.where(start_mask == False)[0]
    fitnesses = []

    nbp = len(paths)

    # for each path, start and end column
    css = np.array([path.cs for path in paths])
    ces = np.array([path.ce for path in paths])

    # for each path, a fast index structure to lookup path index for a given column
    # index = np.array([path.col_index for path in paths])

    # for each path, the start and end index in the path
    pis = np.zeros(nbp, dtype=np.int32)
    pjs = np.zeros(nbp, dtype=np.int32)

    # for each path, the start and end index of its induced segment
    iss = np.zeros(nbp, dtype=np.int32)
    ies = np.zeros(nbp, dtype=np.int32)

    # for each path, the sum of similarities on its induced path
    sim = np.zeros(nbp, dtype=np.float64) 

    # 1 means relevant
    pmask = np.full(nbp, False)

    for s in ss:

        if np.any(mask[s:s+l_min]):
            continue

        pmask = (css <= s) & (s <= (ces - l_min))
        sim   = np.zeros(nbp, dtype=np.float64)

        # initialize 
        for p in np.flatnonzero(pmask):
            path   = paths[p]
            pis[p] = pi = path.find_col(s)
            pjs[p] = pj = path.find_col(s + l_min - 1 - 1)
            iss[p] = path[pi][0]
            ies[p] = path[pj][0] + 1
            if np.any(mask[iss[p]:ies[p]]):
                pmask[p] = False
                continue
            sim[p] = np.sum(path.sims[pi:pj+1])
        
        for e in range(s + l_min, min(n + 1, s + l_max + 1)):

            if mask[e-1]:
                break

            pmask = pmask & (ces >= e)

            # no match
            if not np.any(pmask[1:]):
                break
            
            for p in np.flatnonzero(pmask):
                path = paths[p]
                pj   = path.find_col(e-1)
                ie   = path[pj][0] + 1

                if np.any(mask[ies[p]:ie]): # or ies[p] - iss[p] < l_min or ies[p] - iss[p] > l_max:
                    pmask[p] = False

                ies[p] = ie
                sim[p] += np.sum(path.sims[pjs[p]+1:pj+1])
                pjs[p] = pj

            if not np.any(pmask[1:]):
                break

            # non relevant paths do not contribute
            sim[~pmask] = 0.0

            if end_mask[e-1]:
                continue

            # from here on only consider unmasked
            # sort iss and ies
            iss_ = iss[pmask]
            ies_ = ies[pmask]

            perm = np.argsort(iss_)
            iss_ = iss_[perm]
            ies_ = ies_[perm]

            skip = False
            overlaps = []
            # check overlap
            for i in range(1, len(iss_)):
                if ies_[i - 1] > iss_[i] + 1:
                    overlap = ies_[i - 1] - (iss_[i] + 1)
                    # if overlap > allowed_overlap:
                    if overlap > allowed_overlap * (ies_[i - 1] - iss_[i - 1]) // 2 or overlap > allowed_overlap * (ies_[i] - iss_[i]) // 2:
                        skip = True
                        break
                    overlaps.append(overlap)

            if skip:
                if pruning:
                    break
                else:
                    continue

            coverage = np.sum(ies_ - iss_) - np.sum(np.array(overlaps))
            n_coverage = (coverage - (e - s)) / float(n)

            score = np.sum(sim)
            total_length = np.sum((pjs[pmask] - pis[pmask] + 1))

            n_score = (score - (e - s)) / float(total_length)

            fit = 0
            if n_coverage != 0 or n_score != 0:
                fit = 2 * (n_coverage * n_score) / (n_coverage + n_score)

            # Calculate the fitness value
            if fit > 0:
                fitnesses.append((s, e, fit, n_coverage, n_score))

    return fitnesses


# @njit(cache=True, parallel=True)
# @njit(cache=True)
def _calculate_fitnesses(start_mask, end_mask, mask, paths, l_min, l_max, allowed_overlap=0, pruning=True):
    fitnesses = []

    n = len(mask)

    css = np.array([path.cs for path in paths])
    ces = np.array([path.ce for path in paths])

    nbp = len(paths)

    pis = np.zeros(nbp, dtype=np.int32)
    pjs = np.zeros(nbp, dtype=np.int32)
    iss = np.zeros(nbp, dtype=np.int32)
    ies = np.zeros(nbp, dtype=np.int32)

    # 1 means relevant
    pmask = np.full(nbp, False)

    for s in range(n - l_min + 1):
        # check start mask and mask
        if start_mask[s] or mask[s]:
            continue

        pmask = (css <= s) & (s <= (ces - l_min))
        # no match
        if not np.any(pmask[1:]):
            continue

        # this can be vectorized
        for p in np.flatnonzero(pmask):
            path   = paths[p]
            pis[p] = pjs[p] = pi = path.find_col(s)
            iss[p] = path[pi][0]

        psims = np.zeros(nbp) 

        for e in range(s + 2, min(n + 1, s + l_max + 1)):
            
            # print(e)
            pmask = pmask & (ces >= e)

            # this can be vectorized
            for p in np.flatnonzero(pmask):
                path = paths[p]
                pj   = path.find_col(e-1)
                ie   = path[pj][0] + 1
                # update mask
                pmask[p] = not np.any(mask[ies[p]:ie]) # or ies[p] - iss[p] < l_min or ies[p] - iss[p] > l_max:
                # update sims
                psims[p] += np.sum(path.sims[pjs[p]:pj+1])
                ies[p] = ie
                pjs[p] = pj+1

            if (e - s) < l_min:
                continue

            if not np.any(pmask[1:]):
                break

            # check end mask
            if end_mask[e-1]:
                continue

            # sort iss and ies
            iss_ = iss[pmask]
            ies_ = ies[pmask]

            perm = np.argsort(iss_)
            iss_ = iss_[perm]
            ies_ = ies_[perm]

            # overlaps   
            len_      = ies_ - iss_
            len_[:-1] = np.minimum(len_[:-1], len_[1:])
            overlaps  = np.maximum(ies_[:-1] - iss_[1:] - 1, 0)
            
            if np.any(overlaps > allowed_overlap * len_[:-1]): 
                if pruning:
                    break
                else:
                    continue

            # scores
            coverage   = np.sum(ies_ - iss_) - np.sum(overlaps)
            n_coverage = (coverage - (e - s)) / float(n)

            score   = np.sum(psims[pmask])
            n_score = (score - (e - s)) / float(np.sum(pjs[pmask] - pis[pmask] + 1))

            fit = 0
            if n_coverage != 0 or n_score != 0:
                fit = 2 * (n_coverage * n_score) / (n_coverage + n_score)

            # Calculate the fitness value
            if fit > 0:
                fitnesses.append((s, e, fit, n_coverage, n_score))

    return fitnesses