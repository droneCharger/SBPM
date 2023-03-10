import sbpm.satisfy_capacity
import sbpm.find_min_deadline
import sbpm.comput_length
import sbpm.compute_passengers
def satisfy_length_constraint(final_path,deadlines,t1_max,t2_max,speed,graph,passengers):
    final_path_length = sbpm.comput_length.comput_length(final_path, graph)
    path_capacity = sbpm.compute_passengers.compute_passengers(final_path, passengers)
    min_deadline = sbpm.find_min_deadline.find_min_deadline(final_path, deadlines)
    path_length_constraint = \
        speed*(min_deadline-path_capacity*(t1_max+t2_max))
    while final_path_length > path_length_constraint:
        final_path.pop()
        final_path_length = sbpm.comput_length.comput_length(final_path, graph)
        path_capacity = sbpm.compute_passengers.compute_passengers(final_path, passengers)
        path_length_constraint = \
            speed * (sbpm.find_min_deadline.find_min_deadline(final_path, deadlines) - path_capacity * (
                        t1_max + t2_max))
    return final_path