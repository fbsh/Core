let mmt l = 
    let s1 = List.sort compare l in
    let rec find = function
        | [] -> None
        | x::[] -> Some (x+1)
        | x::y::_ when y - x > 1 -> Some (x+1)
        | _::t1 -> find t1
    in
    find((-1)::s1);;
