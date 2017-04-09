---- .aligncenter .bg-black
@unsplash(SKcTKYNRvHY) .light

@h3 .text-data **twitter amplifers** 
@h4 A glimpse into the alt-right
  
@footer @div .wrap @div .span
 @button(href="https://github.com/thoppe/presentation-twitter-amplifers") .alignleft .ghost
   ::github:: Project repo
 @button(href="https://twitter.com/metasemantic") .ghost .alignright
   ::twitter:: @metasemantic 

----  .bg-black .slide-top
@background(url="https://cdn-images-1.medium.com/max/1200/1*z35xZD_H8RkyAEtSz-RVBA.jpeg")

@div .wrap .content-left
     @h1 **Data for Democracy**
     @h2 hackathon!

---- .wrap

@div @h2 
	With the rise of pseudo-news,<br>
	bots, and mainstream trolls,<br>
	is there any signal in this noise?<br>
<br><br><br>
hell yes, let's find it. 
---- .align-left .bg-black
@unsplash(pb_lF8VWaPU) .dark

@h1 hey twitter
What does an echo chamber look like?

@p
	+ Can we distinguish people inside and out?
	+ Do accounts have multiple chambers?
	+ Can this be done programmaticly?

---- .align-left .bg-apple
@unsplash(Dn-BqRT9RBk) .dark

@h1 Methodology
+ Start with a target user
+ Collect all followers accounts to the user
+ Collect all tweets from these followers
+ Hash all tweets and find those similair (via [Simhash](https://github.com/leonsim/simhash))
+ Compute a similarity score between all accounts
+ Cluster accounts on similairty

---- .aligncenter .bg-black

@h1 **@metasemantic**
@figure(src="metasemantic.png" height=600px)



---- .align-left .bg-black					
@unsplash(7BiMECHFgFY)

.text-landing Slide 5
@h2 _pretty code blocks_
Syntax highlighting Google's [code prettify](https://github.com/google/code-prettify)  

```
sort [] = []
sort (x:xs) = sort lower ++ [x] ++ sort higher
    where
        lower = filter (< x) xs
        higher = filter (>= x) xs
```
Code blocks are context-aware
```
// to convert prefix to postfix
main() {
  char c = getchar();
  (c == '+' || c == '-' || c == '*' || c == '/') ? main(), main() : 0;
  putchar(c);
} 
```

----- .slide-top
@background_video(https://cdn.shutterstock.com/shutterstock/videos/15778135/preview/stock-footage-office-chair-race-slow-motion-young-guys-have-fun-in-the-office-during-a-break-games-of-businessm.mp4)

.text-landing Slide 6
@h2 _looping background animations_
Embed/hotlink any video file (thanks [Shutterstock](https://www.shutterstock.com/)!)

---- .slide-bottom .bg-black
@unsplash(U5rMrSI7Pn4) .light

.content-center .text-shadow 
  @h1 .text-landing **A pug and an Equation**
  @h3 $i \hbar \frac{\partial}{\partial t}\Psi(\mathbf{r},t) = \hat H \Psi(\mathbf{r},t)$
  
@footer this slide looks important right? It's not!

----- .bg-apple

# .text-data Thanks, you!

@footer
  @h4 Contribute at
  @h2 [https://github.com/thoppe/miniprez](https://github.com/thoppe/miniprez)