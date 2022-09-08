let p x l =
    let f (num_less, left, right) y =
        if y < x then num_less + 1, y::left, right
        else num_less, left, y::right
    in
    List.fold_left f(0, [], []) l;;

let min_missing l =
    let rec find lo = function
        | [] -> lo
        | x::tl ->
                let num_less, left, right = p x tl in
                if num_less + lo = x then find (x+1) right
                else find lo left
    in
    find 0 l;;
