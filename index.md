---- .aligncenter .bg-black
@unsplash(SKcTKYNRvHY) .light

@h3 .text-data **twitter amplifers** 
@h4 A glimpse into the alt-right
  
@footer @div .wrap @div .span
 @button(href="https://github.com/thoppe/presentation-twitter-amplifers") .alignleft .ghost
   ::github:: Project repo
 @button(href="https://twitter.com/metasemantic") .ghost .alignright
   ::twitter:: @metasemantic 

----  .bg-black

@background(url="https://cdn-images-1.medium.com/max/1200/1*z35xZD_H8RkyAEtSz-RVBA.jpeg")

@div .wrap
     @h1 **Data for Democracy**
     @h2 hackathon!

---- .align-left .bg-white

@div .wrap .size-50 

  @h1 .text-landing The solution: <br> miniprez
  @line
  @p A [python library](https://github.com/thoppe/miniprez) written using
     [pyparsing](http://pyparsing.wikispaces.com/) and
     [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).
     Miniprez compiles [text](tutorial.md) into a single-page html presentation
     (like this one) with extra goodies. Emoji, font-awesome, LaTeX, and code
     highlighting are built in. Full-screen backgrounds and video can render behind
     the each screen. Slides are controlled with page-up and page-down and scrolled
     easily on mobile.

---- .align-left .bg-black
@unsplash(F1dSr7I4AmY) .dark

.text-landing .text-content _Slide 2_
@h2 _simple markdown support_
Basic [Markdown](https://daringfireball.net/projects/markdown/syntax) with tweaks!

@line

@h3 
 + :muscle: **bold** `**text**`
 + :fire: *fire* `*text*`
 + :cloud: _emph_ `_text_`
 + :computer: `code` `&&&`code&&&`` 

---- .align-left .bg-apple
@unsplash(pmX9BkDDr_A) .light

.text-landing Slide 3
@h2 _emoji_
Standard emoji and [font-awesome](http://fontawesome.io/)  
@line

.grid @h3
  | `:battery:` :battery:
  | `:heart_eyes:` :heart_eyes:
  | `::meetup::` ::meetup::
  | `::ra::` ::ra:: 

---- .bg-apple .align-left
@unsplash(5mZ_M06Fc9g) .dark

.text-landing Slide 4
@h2 _math support_
LaTeX rendered inline with [KaTex](https://github.com/Khan/KaTeX)  
@line
@h3 $P(x)=\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{(x-\mu)^2}{2\sigma ^2}}$
<br>
`$P(x)=\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{(x-\mu)^2}{2\sigma ^2}}$`

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