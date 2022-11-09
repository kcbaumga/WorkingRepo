fn main() {
    let s1=String::from("hello");
    let len=calculate_length(&s1);

    println!("The length off '{}' is {}", s1, len);

    let mut r =String::from("sup");
    change(&mut r);
    println!("{r}");


    //This is confusing af
    let mut a =String::from("hello");
    let a1=&a;
    let a2=&a;

   // let a3=&mut a;
   //println!("{}, {}, and {}", a1, a2, a3) cant do this

   //let mut a3=&a;
   //println!("{}, {}, and {}", a1, a2, a3) // can do this

   println!("{} and {}", a1, a2);// can also do this from 23-26

   let a3=&mut a;
   println!("{}", a3);

   let reference_to_nothing=dangle();
   //cdprintln!("{reference_to_nothing}")
}
fn calculate_length(s:&String)->usize{
    s.len()

}

fn change(some_string: &mut String){
    some_string.push_str(" dude!!!!!");
}
fn dangle()-> String{
    let s=String::from("hi man");
    //&s pointer reference errors here need blank s
    s
}