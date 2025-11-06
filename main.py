 from flet import *

def main(page: Page):
    page.bgcolor = "cyan"
    page.scroll = "auto"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    text_field = TextField(
        label="Email",
        helper_text="example@gmail.com",
        color="green",
        bgcolor="white",
        icon=Icons.EMAIL,
        width=350
    )

    t2 = TextField(
        label="Password",
        helper_text="Enter your password",
        color="green",
        bgcolor="white",
        icon=Icons.LOCK,
        width=350,
        password=True,
        can_reveal_password=True
    )

    # ✅ استخدام الخاصية الصحيحة image=
    container = Container(
        content=Column(
            [
                text_field,
                t2
            ],
            alignment="center",
            horizontal_alignment="center",
        ),
        width=page.width,
        height=page.height,
        image=Image(  # هنا نضع صورة الخلفية
            src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTDWEH2kRbAwXOu00VPkP7OWL1N7aDAbOmh9xtvkNIc4YRXKD0q8HjfR3Wr&s=10",
            fit=ImageFit.COVER
        ),
    )

    page.add(container)
    page.update()

app(target=main)
