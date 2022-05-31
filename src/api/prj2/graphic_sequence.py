import logging as log
import random


def _find_max_index(list):
    max = -1;
    max_index = -1

    for iter in range(len(list)):
        if list[iter] > max:
            max = list[iter]
            max_index = iter
    
    return max_index


def _is_all_zero(list) -> bool:
    for el in list:
        if el != 0:
            return False
    else:
        return True


def generate_with_graphic_sequence(input_gseq):
    if not is_graphic_sequence(input_gseq):
        log.error("Given degree sequence is not a graphic sequence!")
        return [[] for i in range(len(input_gseq))]

    gseq = input_gseq.copy()
    log.info(gseq)

    adjacency_list = [[] for i in range(len(gseq))]

    while not _is_all_zero(gseq):
        log.debug("==== NEXT ITERATION ====")
        log.debug(gseq)
        max = _find_max_index(gseq)
        log.debug(f"max = {max}")
        skip = 0
        edge_index = 0
        node_degree = gseq[max]
        dirty_hack_guard = -1
        while edge_index < node_degree:
            log.debug(f"edge_index = {edge_index}, skip = {skip}")
            target = ((max+1) + edge_index + skip) % len(gseq)
            log.debug(f"target = (max+1+edge_index+skip)%{len(gseq)} = {((max+1) + edge_index + skip)}%{len(gseq)} = {target}")

            if edge_index == 0: # find second max value's index
                temp = gseq[max]
                gseq[max] = 0
                target = _find_max_index(gseq)
                dirty_hack_guard = target
                gseq[max] = temp
                log.debug(f"Overriding target = {target}")
            
            if (edge_index != 0) and (target == dirty_hack_guard):
                log.debug(f"target = {target} guarded by dirty hack, SKIPPING")
                skip += 1
                continue

            if target == max:
                log.debug(f"target == max, SKIPPING")
                skip += 1
                continue

            if gseq[target] <= 0:
                log.debug(f"gseq[target] = {gseq[target]} <= 0, SKIPPING")
                skip += 1
                continue

            log.debug(f"gseq[target] = {gseq[target]} > 0")
            adjacency_list[max].append(target+1)
            adjacency_list[target].append(max+1)
            gseq[target] -= 1
            gseq[max] -= 1

            edge_index += 1
            log.debug(f"adjacency_list = {adjacency_list}")

    return adjacency_list


def is_graphic_sequence(input_seq) -> bool:
    seq = input_seq.copy()
    if len(seq) <= 1:
        log.info("Number of vertices is smaller than 1, returning FALSE")
        return False
    
    odd = 0; even = 0
    for el in seq:
        if el%2 == 0:
            even += 1
        else:
            odd += 1
    log.info(f"Odd elements: {odd}, even elements: {even}")
    if odd%2 != 0:
        log.info(f"Number of odd vertices is odd, returning FALSE")
        return False
    
    log.info(f"Sequence length is {len(seq)}")
    
    seq.sort()
    seq = seq[::-1]  # reverse
    log.info(seq)
    
    while True:
        log.debug("Next iteration")
        log.debug(seq)

        is_all_zero = True
        for el in seq:
            log.debug(f"is_all_zero({is_all_zero}) &= (el({el}) == 0) --> {is_all_zero & (el == 0)}")
            is_all_zero &= (el == 0)
            if not is_all_zero:
                break

        if is_all_zero == True:
            log.info(f"All elements are zero, returning TRUE")
            return True

        if seq[0] >= len(seq):
            log.info(f"seq[0] is either <0 or >=len(seq), returning FALSE")
            return False

        for el in range(0, len(seq)):
            log.debug(f"seq[el] < 0 --> seq[{el}] < 0 --> {seq[el]} < 0 --> {seq[el] < 0}")
            if seq[el] < 0:
                log.info(f"seq[el] < 0, returning FALSE")
                return False

        for i in range(1, seq[0]+1):
            seq[i] -= 1
        
        seq[0] = 0
        seq.sort()
        seq = seq[::-1]  # reverse


def _edge_count(adj_list):
    summ = 0
    for node in adj_list:
        summ += len(node)
    log.debug(f"Sum = {summ}")
    return summ


def _max_edge_count(adj_list):
    return len(adj_list) * (len(adj_list)+1) / 2


def generate_simple_graph_with_graphic_sequence(gseq, swap_count):
    if not is_graphic_sequence(gseq):
        log.error("Given degree sequence is not a graphic sequence!")
        return [[] for i in range(len(gseq))]

    adjacency_list = generate_with_graphic_sequence(gseq)
    log.debug(f"Start: Adjacency list = {adjacency_list}")

    if _edge_count(adjacency_list) >= _max_edge_count(adjacency_list)-2:
        log.warn(f"No suitable candidate edges to swap")
        return adjacency_list

    for _ in range(swap_count):
        log.debug("=== NEXT SWAP ===")
        while True:
            x1, y1 = random.sample(list(range(1, len(adjacency_list)+1)), k=2)
            log.debug(f"From {list(range(1, len(adjacency_list)+1))} picked elements x1={x1} and y1={y1}")

            if (y1 not in adjacency_list[x1-1]) and (len(adjacency_list[x1-1]) > 0) and (len(adjacency_list[y1-1]) > 0):
                x2 = random.sample([node for node in adjacency_list[x1-1] if node != x1], k=1)[0]
                y2 = random.sample([node for node in adjacency_list[y1-1] if node != y1], k=1)[0]
                log.debug(f"From {[node for node in adjacency_list[x1-1] if node != x1]} picked x2={x2}")
                log.debug(f"From {[node for node in adjacency_list[y1-1] if node != y1]} picked y2={y2}")

                if (x2 == y2) or (y2 in adjacency_list[x2-1]) and ((x2 in adjacency_list[y1-1]) or (y2 in adjacency_list[x1-1])):
                    pass
                else:
                    adjacency_list[x1-1].remove(x2)
                    adjacency_list[x2-1].remove(x1)
                    adjacency_list[y1-1].remove(y2)
                    adjacency_list[y2-1].remove(y1)

                    if x2 not in adjacency_list[y2-1]:
                        temp = y1
                        y1 = y2
                        y2 = temp
                    
                    adjacency_list[x1-1].append(y1)
                    adjacency_list[y1-1].append(x1)
                    adjacency_list[x2-1].append(y2)
                    adjacency_list[y2-1].append(x2)
                    break

        log.debug(f"Adjacency list = {adjacency_list}")

    return adjacency_list
