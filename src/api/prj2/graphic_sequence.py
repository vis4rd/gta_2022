import logging as log
import random
from re import I

# Assumes that the input is a graphic sequence, returns adjacency list
def generate_with_graphic_sequence(input_gseq):
    gseq = input_gseq.copy()
    log.info(gseq)

    adjacency_list = [[] for i in range(len(gseq))]

    i = 0
    while True:
        if (i < 0) or ((gseq[i] == 0) and (i == len(gseq)-1)):
            log.debug("Used all possibilities, breaking the loop")
            break

        log.debug("Next iteration")
        log.debug(gseq)

        # Find the index of greatest value
        max_val = -1
        max_index = -1
        second_max_index = -1
        for val in range(len(gseq)-1):
            if (gseq[val] > max_val) and (gseq[val] > 0):
                max_val = gseq[val]
                second_max_index = max_index
                max_index = val
        i = max_index
        if i < 0:
            continue

        log.debug(f"i = {i}, gseq[i] = {gseq[i]}")

        if gseq[i] > 0:
            neighbor = second_max_index
            while (neighbor < 0) or (gseq[neighbor] < 1) or (neighbor == i):
                neighbor = random.randint(0, len(gseq)-1)
                log.debug(f"neighbor = {neighbor}")
            log.debug(f"gseq[{i}] > 0, neighbor = {neighbor}")
            adjacency_list[i].append(neighbor+1)
            adjacency_list[neighbor].append(i+1)
            gseq[i] -= 1
            gseq[neighbor] -= 1

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


def generate_simple_graph_with_graphic_sequence(gseq, swap_count):
    adjacency_list = generate_with_graphic_sequence(gseq)
    log.debug(f"Start: Adjacency list = {adjacency_list}")

    for ii in range(swap_count):
        log.debug(f"Swap iteration {ii}")
        while True:
            log.debug(f"Adjacency list = {adjacency_list}")
            x1, y1 = random.sample(range(1, len(adjacency_list)), k=2)
            log.debug(f"From {range(len(adjacency_list))} picked elements x1={x1} and y1={y1}")

            if (y1 not in adjacency_list[x1-1]) and (len(adjacency_list[x1-1]) > 0) and (len(adjacency_list[y1-1]) > 0):
                x2 = random.sample([vertex for vertex in adjacency_list[x1-1] if vertex != x1], k=1)[0]
                y2 = random.sample([vertex for vertex in adjacency_list[y1-1] if vertex != y1], k=1)[0]
                log.debug(f"From {range(len(adjacency_list))} picked elements x2={x2} and y2={y2}")

                if (x2 == y2) or (y2 in adjacency_list[x2-1]) and ((x2 in adjacency_list[y1-1]) or (y2 in adjacency_list[x1-1])):
                    pass
                else:
                    log.debug(f"Removing {x2} from {adjacency_list[x1-1]}")
                    log.debug(f"Removing {x1} from {adjacency_list[x2-1]}")
                    log.debug(f"Removing {y2} from {adjacency_list[y1-1]}")
                    log.debug(f"Removing {y1} from {adjacency_list[y2-1]}")
                    adjacency_list[x1-1].remove(x2)
                    adjacency_list[x2-1].remove(x1)
                    adjacency_list[y1-1].remove(y2)
                    adjacency_list[y2-1].remove(y1)
                    if x2 not in adjacency_list[y2-1]:
                        adjacency_list[x1-1].append(y1)
                        adjacency_list[y1-1].append(x1)
                        adjacency_list[x2-1].append(y2)
                        adjacency_list[y2-1].append(x2)
                    else:
                        adjacency_list[x1-1].append(y2)
                        adjacency_list[y2-1].append(x1)
                        adjacency_list[x2-1].append(y1)
                        adjacency_list[y1-1].append(x2)
                    break

    return adjacency_list

def _has_edge(adj_list, head, tail):
    for el in adj_list[head]:
        if el == tail:
            return True
    return False
