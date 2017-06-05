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
	+ Can this be done in a programmatic way?

---- .align-left .bg-apple
@unsplash(Dn-BqRT9RBk) .dark

@h1 Methodology
@p
	+ Start with a target user
	+ Collect all followers accounts to the user
	+ Collect all tweets from these followers
	+ Clean tweets, remove links, reduce emoji, :smile:
	+ Hash all tweets and find those similar, via [Simhash](https://github.com/leonsim/simhash)
	+ Compute a similarity score between all accounts
	+ Cluster accounts on similarity

---- .aligncenter .bg-black

@h1 **@metasemantic** (that's me!)
@figure(src="figures/metasemantic.png" height=600px)
No real communities, no large following

---- .bg-black

@h1 **@RichardBSpencer**
@h3  white supremacist, alt-right
<br>
.wrap @h4
	"Hail Trump, hail our people, hail victory!" Spencer has popularized the term 'alt-right' to describe the movement he leads. Spencer has said his dream is 'a new society, an ethno-state that would be a gathering point for all Europeans,' and has called for 'peaceful ethnic cleansing.'


@footer still can't recall him?

---- .bg-black
@background_video(src="figures/RS_punch.mp4")
@h1 **@RichardBSpencer**

---- .bg-black .aligncenter
@h3 **@RichardBSpencer** followers (5/55K), Feb-Mar tweets
@figure(src="figures/SG_unorg.png")
unordered

---- .bg-black .aligncenter
@h3 **@RichardBSpencer** followers (5/55K)
@figure(src="figures/SG_large.png")
clustered

---- .bg-black .aligncenter
@h3 **@RichardBSpencer** followers (5/55K)
@figure(src="figures/SG_degree.png")
sorted by degree -- there's a natural dimension of connectivity

---- .bg-black .aligncenter
@h4 Do simple word clouds tell us anything?

Not much difference between low degree
@figure(src="figures/qmin.png")

and high degree
@figure(src="figures/qmax.png")

---- .bg-black .aligncenter
But some words clearly correlate with the distance
@figure(src="figures/word_freq.png")


---- .bg-black

@h1 **@passionatechica**, joined Oct 2016, 
@h3  bot/troll army account, auto follows, ~250 tweets/day
@figure(src="figures/BP_cap.png")

---- .bg-black .aligncenter
@h3 **@passionatechica** following
@figure(src="figures/BP_ordered.png")
sorted by degree -- notice an external community

---- .bg-black .aligncenter
@h3 **@passionatechica** following 
@figure(src="figures/BP_large.png")
cluster -- clear external community (Sanders supporters!?)

----- .bg-apple

# .text-data Thanks, you!

@footer
  @h4 Thoughts? Ideas? Want to contribute?
  @h2 [@metasemantic](href="https://twitter.com/metasemantic")

