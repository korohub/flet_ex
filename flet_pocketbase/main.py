from flet import *
from pocketbase import PocketBase
client = PocketBase("http://127.0.0.1:8090")


def main(page: Page):
    page.scroll = "auto"
    username = TextField(label='username')
    email = TextField(label='email')
    password = TextField(label='password')

    editid = TextField()
    listalluserresult = Column()

    def addnewuser(e):
        try:
            record = client.collection("users").create(body_params={
                "username":username.value,
                "email":email.value,
                "password":password.value,
                "passwordConfirm":password.value,
                "name":username.value
            })
            print(record)
            listalluserresult.controls.clear()            
            get_all_user()

            page.snack_bar = SnackBar(Text("success add user", size=30), bgcolor="blue")
            page.snack_bar.open = True
            page.update()

            
        except Exception as err:
            print(err)

    def deleteuser(e):
        youdeleteid = e.control.data
        admin_data = client.admins.auth_with_password("hamster@gmail.com", "nEXg0V8G3H9Th_dgF-9NFw4kXoDCh0DT")
        alluser = client.collection("users").delete(youdeleteid)
        listalluserresult.controls.clear()
        get_all_user()

        page.snack_bar = SnackBar(Text("Success delete", size=30), bgcolor="red")
        page.snack_bar.open = True
        page.update()

    def savedatanow(e):
        admin_data = client.admins.auth_with_password("hamster@gmail.com", "nEXg0V8G3H9Th_dgF-9NFw4kXoDCh0DT")
        alluser = client.collection("users").update(editid.value, {
            "username": username.value,
            "email":email.value
        })
        listalluserresult.controls.clear()
        get_all_user()
        dialog.open = False
        page.snack_bar = SnackBar(Text("Modifying  Succes", size=30), bgcolor="green500")
        page.snack_bar.open = True
        page.update()

    dialog = AlertDialog(
        title=Text('Edit data'),
        content=Column([
            username,
            email,
        ]),
        actions=[
            TextButton("Save data", on_click=savedatanow)
        ]
    )

    def edituser(e):
        editid.value = e.control.data.id
        username.value = e.control.data.username
        email.value = e.control.data.email
        page.dialog = dialog
        dialog.open = True
        page.update()


    def get_all_user():
        admin_data = client.admins.auth_with_password("hamster@gmail.com", "nEXg0V8G3H9Th_dgF-9NFw4kXoDCh0DT")
        alluser = client.collection("users").get_full_list()
        
        for u in alluser:
            listalluserresult.controls.append(
                Container(
                    bgcolor="blue200",
                    padding=10,
                    content=Column([
                        Row([Text(u.username, size=25, weight="bold", color="black"),Text(u.created)], alignment="spaceBetween"),
                        Text(f'email: {u.email}'),
                        Text(f'verified: {u.verified}'),
                    IconButton("Delete", bgcolor="red700", icon_color="white",data=u.id, on_click=deleteuser),
                    IconButton("Edit", bgcolor="blue", icon_color="white", data=u, on_click=edituser),
                    ],alignment="spaceBetween")
                )
            )
        page.update()
    
    get_all_user()

    page.window_height = 740
    page.window_width = 360
    page.add(
        Column([
            Text("Pocketbase user crud", size=30),
            username,
            email,
            password,
            ElevatedButton("add new user",
                           bgcolor="blue", color="white", on_click=addnewuser)
        ]),
        listalluserresult
    )


app(main)