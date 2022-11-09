fn main() {
    let mut user1=User{
        email: String::from("someone@example.com"),
        username: String::from("someoneuser123"),
        active: true,
        sign_in_count:1,
    };
    user1.email=String::from("differentemail@example.com");

    let user2=User{
        active:user1.active,
        username:user1.username,
        email:String::from("athirdexample@example.com"),
        sign_in_count:user1.sign_in_count,
        //could also use this for same effect, less code:
        //email::String::from("athirdexample@example.com"),
        //..user1
    };
    let black=Color(0,0,0);
    let origin=Point(0,0,0);

    let subject=AlwaysEqual;
}

fn build_user(email: String, username: String)->User{
    User{
        email:email,
        username:username,
        active:true,
        sign_in_count:1,

    }
}
struct User{//standard struct
    active:bool,
    username:String,
    email:String,
    sign_in_count:u64,
            //could also use username:&str,
        //email: &str, will be explained how to make it compile. does not compile like this
}
struct Color(i32,i32,i32);//tuple structs
struct Point(i32,i32,i32);

struct AlwaysEqual;//Unit like struct w/o field