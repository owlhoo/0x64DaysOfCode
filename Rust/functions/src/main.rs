fn main() {
    let x = 5;

    let y = {
        let x = 3;
        x + 1
    };

    println!("x:{} y:{}", x, y);
    println!("funct ret: {} {}", five_six().0, five_six().1,);
    branching();
    exit_function(42.0);
}


fn branching() {
    let mut x= String::new();
    println!("Enter choice: ");

    std::io::stdin().read_line(&mut x)
        .expect("Failed to read a choice");

    let x: i32 = match x.trim().parse(){
        Ok(num) => num,
        Err(_) => return,
    };

    if x == 0 {
        println!("The choice was zero ");
    } else {
        println!("The choice was {} ", x);
    }
}


fn five_six() -> (i32, i32) {
    (5, 6)
}


fn exit_function(x:f64) {
    println!("The program is ending {}.. bye", x);
}