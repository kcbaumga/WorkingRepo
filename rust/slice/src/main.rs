fn main() {
   let mut s=String::from("Hello World");

   let word=first_word(&s);
   println!("{word}");
   s.clear();
   
   let my_string=String::from("hello world");
   let word=first_word(&my_string[0..6]);
   let word=first_word(&my_string[..]);

   let my_string_literal="hello world";
   let word=first_word(&my_string_literal[0..6]);
   let word=first_word(&my_string_literal[..]);

   //array slices
   let aa=[1,2,3,4,5];
   let slice=&aa[1..3];
   assert_eq!(slice, &[2,3]);

}
fn first_word(s: &str) -> &str{//use str instead of String lets us use both
    let bytes=s.as_bytes();

    for (i, &item) in bytes.iter().enumerate() {
        if item==b' '{
            //return i;
            return &s[0..i]
        }
    }
    //s.len()
    &s[..]
}

//fn second_word(s: &String)->&str{


//}