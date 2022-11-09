
fn main() {//test program
    let scale=2;
    let width1=30;
    let height1=50;
    //let rect1=(30,50);
    let rect1=Rectangle{
        width: 30,
        height:50,
    };
    let rect2=Rectangle{
        width:10,
        height:40,

    };
    let rect3=Rectangle{
        width:60,
        height:45,
    };
    println!("rect1 is {:#?}", rect1);

    println!("The area of the rectangle is {} square pixels",
    rect1.area());

    if rect1.width(){
        println!("The rectangle has a nonzero width, it is {}", rect1.width);
    }

    println!("Can rect1 hold rect2? {}", rect1.can_hold(&rect2));
    println!("Can rect1 hold rect3? {}", rect1.can_hold(&rect3));
//area(width1, height1));
   // area(&rect1)); not needed with area method
   

    
}
//fn area(width:u32, height:u32)->u32{
//    width*height
//}
//fn area(dimensions:(u32,u32))-> u32{
    //dimensions.0*dimensions.1// less clear method
//    area(&rect1)
//}
#[derive(Debug)]// goes right before struct it is implemented on
struct Rectangle{
    width:u32,
    height:u32,
}
impl Rectangle{
    fn area(&self)->u32{
        self.width*self.height
    }
    fn width(&self)->bool{
        self.width>0
    }
    fn can_hold(&self, other: &Rectangle)-> bool{
        self.width> other.width&&self.height>other.height
    }
    fn square(size:u32)-> Self{
        Self{
            width:size,
            height:size,
        }
    }
}
fn area(rectangle: &Rectangle)->u32{
    rectangle.width*rectangle.height
}