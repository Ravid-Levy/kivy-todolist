from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.list import MDList, OneLineListItem
from kivymd.uix.navigationdrawer import MDNavigationLayout, MDNavigationDrawer
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.toolbar import MDTopAppBar

menu = {}

class AppBar(MDTopAppBar):
    def __init__(self, parameter, **kwargs):
        self.root = parameter
        super().__init__(**kwargs)
        self.shadow_color = (0, 0, 0, 0)
        self.type_height = "medium"
        self.headline_text = "Headline medium"
        self.left_action_items = [["arrow-left", lambda x: x]]
        self.right_action_items = [
            ["attachment", lambda x: x],
            ["calendar", lambda x: x],
            ["dots-vertical", lambda x: x],
            ]
        self.pos_hint={"top": 1}
        self.elevation=4
        self.title="MDNavigationDrawer"
        self.left_action_items= [['menu',menu["navbar"].set_state("open")]]

                

    # def nav_drawer_open(self):
    #     nav_drawer = self.root.children[0].ids.nav_drawer
    #     nav_drawer.set_state("open")



class Example(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Dark"
        
        menu["navbar"] = MDNavigationDrawer(
                        MDScrollView(
                            MDList(
                                OneLineListItem(
                                    text="Screen 1",
                                    on_press=self.switch_screen,
                                ),
                                OneLineListItem(
                                    text="Screen 2",
                                    on_press=self.switch_screen,
                                ),
                            ),
                        ),
                        id="nav_drawer",
                        radius=(0, 16, 16, 0),
                    )


        return (
            MDScreen(
               AppBar(self.root),
                MDNavigationLayout(
                    MDScreenManager(
                        MDScreen(
                            MDLabel(
                                text="Screen 1",
                                halign="center",
                            ),
                            name="scr 1",
                        ),
                        MDScreen(
                            MDLabel(
                                text="Screen 2",
                                halign="center",
                            ),
                            name="scr 2",
                        ),
                        id="screen_manager",
                    ),
                   menu["navbar"]
                   ,
                    id="navigation_layout",
                )
            )            
        )


    def switch_screen(self, instance_list_item: OneLineListItem):
        self.root.ids.navigation_layout.ids.screen_manager.current = {
            "Screen 1": "scr 1", "Screen 2": "scr 2"
        }[instance_list_item.text]
        self.root.children[0].ids.nav_drawer.set_state("close")




Example().run()