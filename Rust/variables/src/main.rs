fn main() {
    let mut x = 5;
    println!("The value of x is {}", x);

    x = 6;
    const CONSTANT:u32 = 100_000;
    println!("The value of x is {}\nWhile the constant is {}", x, CONSTANT);

    let y = 5;
    let y = y + 1;
    let y = y * 2;
    println!("The value of y is {}", y);

    let tup: (i32, f64, u8) = (500, 6.4, 1);
    let (x, y, z) = tup;
    println!("The value of z is {}", z);
    println!("The value of z is {}", tup.2);

    let mut array = [1, 2, 3, 4 ,5];
    println!("The value of array[3] is {}", array[3]);

    array[3] = 20;
    println!("The value of array[3] is {}", array[3]);
}
