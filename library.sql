SQLite format 3   @     *                                                               * .WJ   p ��p                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              ��tablereviewsreviewsCREATE TABLE reviews (
	id INTEGER NOT NULL, 
	score INTEGER, 
	comment VARCHAR, 
	book_title VARCHAR, 
	user_id INTEGER, 
	book_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES users (id), 
	FOREIGN KEY(book_id) REFERENCES books (id)
)�r�CtablebooksbooksCREATE TABLE books (
	id INTEGER NOT NULL, 
	title VARCHAR, 
	author VARCHAR, 
	genre VARCHAR, 
	stocked BOOLEAN, 
	owner_id INTEGER, 
	rating INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(owner_id) REFERENCES users (id)
)~�[tableusersusersCREATE TABLE users (
	id INTEGER NOT NULL, 
	username VARCHAR, 
	password VARCHAR, 
	PRIMARY KEY (id)
)   � ����oS3���                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  Demo1234
 +art_appreciatorcreative	 %chef_cuisinedelicious /sports_enthusiastgo_team /cinema_aficionadocinemafan %!music_melodymusiclover  1!wanderlust_trekkerwanderlust 'python_masterpython123 #!lit_lover42ilovebooks '!bookworm_janemypassword %coding_ninjasecret123   � ��}I ���`,���                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               * '%	The AlchemistPaulo CoelhoAdventure/ +-	The RoadCormac McCarthyPost-Apocalyptic% #%	The ShiningStephen KingHorror# ##	The OdysseyHomerEpic Poetry2
 '#1	War and PeaceLeo TolstoyHistorical Fiction)	 +	Moby-DickHerman MelvilleAdventure0 /)	To the LighthouseVirginia WoolfModernist- +'	Brave New WorldAldous HuxleyDystopian2 9'	The Catcher in the RyeJ.D. SalingerFiction' !)	The HobbitJ.R.R. TolkienFantasy2 -3	The Great GatsbyF. Scott FitzgeraldFiction- 3#	Pride and PrejudiceJane AustenClassic" '	1984George OrwellDystopian. 7!	To Kill a MockingbirdHarper LeeFiction   { ��s@��~W0
��{                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       - 9'Life-changing journey.The Alchemist3 OA haunting post-apocalyptic tale.The Road) 5#A bit disappointing.The Shining$ -#	A timeless epic.The Odyssey%
 )'A masterpiece!War and Peace

%	 1An epic adventure!Moby-Dick		/ 5/An interesting read.To the Lighthouse+ 1+Not my cup of tea.Brave New World7 ;9A classic for a reason.The Catcher in the Rye) 7!Absolutely fantastic!The Hobbit1 ;-Could have been better.The Great Gatsby= M3Enjoyed it, but not my top pick.Pride and Prejudice" 5One of my favorites!1984( #7		Great book!To Kill a Mockingbird