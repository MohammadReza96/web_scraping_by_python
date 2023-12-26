class product:
    def __init__(self,img,tile,score,city,pricebefore,discount,pricenow) -> None:
        self.img=img
        self.title=tile
        self.score=score
        self.city=city
        self.pricebefore=pricebefore
        self.discount=discount
        self.pricenow=pricenow
    def __str__(self) -> str:
        return f'{self.img}\n{self.title}\n{self.score}\n{self.city}\n{self.pricebefore}\n{self.discount}\n{self.pricenow}'