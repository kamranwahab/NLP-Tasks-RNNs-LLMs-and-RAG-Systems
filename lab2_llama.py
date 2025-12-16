import requests
import json

# --- CONFIGURATION ---
# Ensure Ollama is running (run 'ollama serve' or just open the app)
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3"

# --- THE DATA FROM YOUR TASK 1 ---
test_data = [
  {
    "text": "? went to see this as me and my lady had little else to do on a sunday afternoon i like films that deal with sleazy loser characters and this is full of em after a slow start we get some good turns from the cast but it is the actual ? that both makes and lets the film down the ? is one of the funniest scenes i have seen in a film for a long while but is too short and could have made this a masterpiece overall ? 2 out of 10",
    "true_label": "Positive"
  },
  {
    "text": "? one of my best friends brought this movie over one night with the words ? watch the worst horror movie ever ' i always enjoy a good laugh at a bad horror flick and said yes i had expected your typical cheesy b slasher but this was beyond b this is z slasher the lowest of the low with obviously low budget extremely bad acting bad lightning no plot really bad so called ? ? shaky cameras and a horrible soundtrack this makes movies like house of wax look like oscar winning masterpieces the only good thing about it is about 15 seconds of one of the characters getting topless she had some very nice tits most of what i said during this film was along the lines of ? this is actually so ? ? is the worst movie ? and ? not drunk enough for ? so in conclusion don't waste your time or money",
    "true_label": "Negative"
  },
  {
    "text": "? really truly ? ? awful but actor ? moore the movie lone ranger ? himself competently as an actor he's the only one br br a rare treat for five minutes if you want to ? the depths of ? transparent special effects southern california as the moon again and again and again and acting so ? inept that it may be a spoof except that it's clear that it isn't no humor here except unintentionally br br the dialogue may be worse than any of these other aspects and the costumes well enough said plot what plot bad guy well head bad guy and his henchmen including his ? agent called ? listen carefully or you'll suspect it's a spoof on the name of ? ? ray ? and his unbelievably inept ? who however have ? that never need ? as does ? cody so there are numerous ? ? br br enjoy",
    "true_label": "Negative"
  },
  {
    "text": "? the biggest reason i had to see this movie was that it stars susan swift an outstanding and all too ? actress time travel movies usually don't interest me and neither do movies about witchcraft but this movie was fascinating and creepy it didn't rely on outrageous special effects and it didn't focus so heavily on the time travel that the viewer gets lost and confused this was a really creative movie kept simple and focused with great acting by all",
    "true_label": "Positive"
  },
  {
    "text": "? this film screened last night at ? paramount theater as part of the ? film festival we were ? with the presence of director mike ? and stars adam sandler and don cheadle who took audience questions after the film it is a remarkable and powerful film about what it is like to lose yourself and begin to find your way back the performances are phenomenal and the story manages to be both tragic and funny in a way that is all too rare the trailer for the film tries a little too hard to emphasize the comedic aspects br br this is a ? role for adam sandler while he has begun to transition to more dramatic roles with punch drunk love and ? this role is a significant step forward for him as a dramatic actor he deserves an oscar nomination as he continues down to transition to more dramatic roles as tom hanks did and jim carrey is also doing in this role he seemed to be trying to channel dustin hoffman in rain man although playing an ? man is certainly very different than ? traumatized character both characters for different reasons are trapped in their own worlds of child like isolation and confusion br br don ? performance is less surprising but just as good after hotel ? and crash we've come to expect remarkable nuanced performances from cheadle he has the qualities of sincerity and honesty that comes through in this role but he too is also broken and struggling if not in the such profound ways as ? character cheadle is struggling with difficulties in both his marriage and in his professional life as a dentist together the characters played by cheadle and sandler struggle to ? each other in the way that true friends often do in a way that reminds me of matt damon and robin williams in good will hunting they are both searching for that part of the themselves that they have lost and trying to find again br br reign over me is one of the best major studio films to be released this year the soundtrack which is almost another character in the plot is wonderful the filming in the streets of new york a city that suffered a great tragedy and has also had to ? itself is also quite beautiful the supporting roles by ? ? smith ? tyler ? ? in a very odd role donald sutherland and mike ? himself are all quite good br br writer director mike ? has really delivered a story that so many will be able to connect with on numerous levels this is a story about grief family healing male friendship mental health and the meaning of love reign over me does not disappoint the film is almost hypnotic as it draws you into the lives of its characters hollywood would have a much better reputation if it made more character driven charming films like reign over me",
    "true_label": "Positive"
  },
  {
    "text": "? i should explain why i gave this piece of art 1 star rating out of possible 10 simply because it's hard or next to impossible to rate it ? probably it would have been the same if i had given it 10 10 explanations anyway would have followed br br i am not fond of these pointless gore movies like hostel or so i think that's disgusting and pretty terrible in all the possible ? meanings but as i found out after watching this movie there is a genre called historical drama and probably it would have been the case of 10 10 as it has plenty of it and tarantino would have been more than happier with it and made kill bill 3 to ? even more blood on screen than here to show that it is possible but the thing about historical drama genre is that it's a sub category of the trash movies where john romero is the undead gory emperor of the guts and so automatically it can't be rated as your ? movie as these are movies that are made bad on purpose and you can't really tell whether the ? bad moment was meant to be so or it was simply bad it's for the people who like to enjoy bad acting bad screenplay and bad everything else and by some turn of faith i am one of them too there are days when i have an urge of seeing a really bad movie and look up for some trash and here you go the day is saved but that's definitely an opinion of mine and doesn't have match with ? else br br what i wanted to say is that if you want to watch some terrible movie then ? ? is definitely the choice but ? my advice and don't rate it by ? means",
    "true_label": "Negative"
  },
  {
    "text": "? i don't often go out of my way to write comments but for this i had to just to warn anyone that might think that by watching this they will see a comedy this doesn't come close while the premise change in colour gender whatever is bad enough and has been done better many times before the actual transformation of two black guys into two white girls is one of the least convincing ? ever put on screen it would be bad enough if all that was required by the script was a change to white chicks however the wayans brothers are required to disguise themselves as two specific white women as you will have guessed by now they fail completely i have seen drag queens without makeup make more convincing women than these two do with the best special effects and make up people that hollywood can provide its appalling add to the mix a basketball player built like a building terrible dialogue and more plot holes than a golf course and this film hits a new personal low and i like bad movies avoid like the plague",
    "true_label": "Negative"
  },
  {
    "text": "? my comments may be a bit of a spoiler for what it's worth stop now if you care enough br br saving grace should have been titled a paper thin excuse for old british women to get high on screen this film is dumb the incidental music is an annoyance as are the obvious hackneyed tunes that ? pop up to comment on the narrative spirit in the sky for example oh i get it this is basically a cheech and chong movie made credible by its ? english setting and brenda ? overwhelming power to ? emotion on an audience using her voice alone i could literally hear the folks over at high times magazine receiving their ? over the enormous ? that ? this picture worst scene easy brenda attempts to ? her ? ? on the street of london in a ? white dress suit not funny not original not interesting not a good movie the 7 2 rating is the result of ? over voting don't waste your time",
    "true_label": "Negative"
  },
  {
    "text": "? for a movie with a plot like this i would normally smell ? in the first ten minutes and turn it off but this was very well made with emotional subtleties great acting and some genuinely funny moments it was also interesting to see a different culture a ? one at that my wife and i both ? it",
    "true_label": "Positive"
  },
  {
    "text": "? i saw this film awhile back while working on a trailer for the film's production company and it was terrible ? is mediocre at best hopkins phones his performance in but still blows away ? in their scenes together and alec looks bored trust me on this you should avoid this film like the plague if it ever gets released it seems to go on forever as the tired plot unfolds at a ? pace it is relentlessly unfunny the cinematography is crappy and the direction is pedestrian alec baldwin should go to film school if he plans to direct again in terms of his acting his character is totally unlikable which makes it impossible to root for him dan ? is pretty funny and the surprising makeup of the jury near the film's end is cute but this film is just plain awful",
    "true_label": "Negative"
  },
  {
    "text": "? in fact marc ? off broadway adaptation of ? was not so ? as is generally believed br br i have a special interest in ? my dad was part of the first full production in the us u of ? theatre ? did it around the end of ww2 ? had been so nearly successful in ? the play that they had to ? the script and score from ? in two different languages neither english a german ? script and similar sources ? adaptation not a translation which had the full ? of ? ? was a lot closer to the original than generally believed br br the problem is that the version thereof that most people know is the mgm cast recording recently available on ? on cd which includes ? arthur as lucy the big complete girl and can't i see her hands on ? and shoulders thrown back on that line ? was a major babe in the 50's paul ? and john ? was heavily ? by mike ? head of mgm records i mean 17 i think it was ? s got cut to just damn br br at one time mgm also offered a 2 ? set of the entire play ? as heavily ?",
    "true_label": "Negative"
  },
  {
    "text": "? blood legacy starts with the arrival of lawyer tom drake norman ? to the dean estate ? owned by the now deceased christopher dean john carradine upon his arrival he is ? by mr ? four children gregory jeff ? his wife laura merry ? victoria faith ? johnny richard ? plus leslie brooke mills her ? carl ? john smith drake plays a tape recording of they're late father's wishes after his death the estate worth ? million dollars is to be split equally between his four children if any should die then the money would be split equally between the rest if all were to die the freaky servants ? ? ? ? buck ? the more ? named frank john russell would pocket the lot well not satisfied with a quarter share of ? million which is still almost 35 million back in 1971 which doesn't sound too bad to me someone decides they want it all for themselves it's not long before decapitated heads are turning up in the ? br br co written produced directed by roy ? blood legacy disappointed me on two accounts for starters this film's alternate much more common title is legacy of blood which is also the title of an obscure horror film directed by andy ? back in ? which i've always wanted to see both films are regularly mixed up as both have similar stories when i checked my on screen cable tv guide for legacy of blood i was excited because it said it was the ? film even listed him as director so when i actually sat down to watch it i heard john ? voice i then knew it wasn't the ? film that i had wanted to see my heart ? then of course there's the simple yet undeniably straight forward fact that blood legacy is a total utter piece of crap that is literally painful to watch at times the script by ? eric ? is slow boring extremely predictable the character's are absolutely bizarre in an annoying way the freak of a servant who ? his sister to ? him the strange set of brother's sisters who are just downright unlikeable so far removed from reality that any tension or mystery that the simplistic ? story could have achieved is sorely missing then there's the awful twist ending that you can guess within the first 10 minutes it's boring to watch it's poorly paced it's just a chore to even think about it please someone save me as this is really bad stuff i could go on all day about how bad blood legacy is i really could br br director ? was either working with a none existent budget or judging by this he shouldn't have even been directing traffic the entire film looks ugly it's poorly photographed there is no atmosphere or scares the blood gore is tame there's an axe in a head a decapitated head a scene when someone is ? to death by ? the best murder when someone's face is eaten by ? however there are question marks over this scene so there's the victim right there's the tank of ? right victims head is placed in ? tank right ? eat victims face right water remains crystal clear despite said victim having his face eaten ? where's the blood br br technically blood legacy is terrible it looks awful the sound was obviously shot live it's ? hard to hear which considering the terrible dialogue is maybe a ? in disguise the acting was not going to win anyone any awards that's for sure the least said about it the better br br blood legacy is an awful film there really isn't a single positive aspect to it or if there is i can't think of it do yourself a favour don't bother with this one there are much better films out there",
    "true_label": "Negative"
  },
  {
    "text": "? i'd really really wanted to see this movie and waited for months to get it through our blockbuster total access account when it showed up in our ? i threw it straight into the dvd player br br i was very sadly disappointed which in turn made me mad i'll give any movie a chance even if i want to walk out of the theater press ? i watched it all the way through but didn't get anything from it but frustration br br the acting was very very good but that was about it nothing is explained while we understand that mathieu becomes depressed and lands in a ? ward of some kind we're never given insight to his ? while we understand that he and cedric break up again we don't see it happen or why it happened during an interview with ? doctor cedric reveals that he'd cheated on him once but it was no big deal i expected to see this in flashbacks but no nothing we also gets the hints that cedric was the one to bring ? to the hospital but again we don't see it br br i know some movies are a ? it as it ? basis but this movie honestly ? me off when pierre ? ex shows up in the club and starts trouble we don't see hide nor hair of him until near the end and it took me a good ? of time to figure out that pierre was the ex his personality at the club and when ? finds him are entirely different i might even be wrong saying this it was that confusing br br the film expects you to know everything and move along with its disjointed out of place and confusing pace i can keep up with films like ? ? ? and other films that have flashbacks flash ? left and right but ? didn't capture and hold onto the style at the end of ? ? you know what's going on and discover the answer to the main mysteries ? just leaves you hanging it has an air of ? in its ? not gonna tell you a damned thing figure it out for ? presentation it's like reading a book with the chapters switched around and pages missing br br good acting like i said i liked the characters but the whole story was just too disappointing",
    "true_label": "Negative"
  },
  {
    "text": "? tashan the title itself explains the nature of the movie br br this type of movies are actually made for flop what a shame that ? raj films produces such movies those are worthless than c grade movies or even some c grade movies have better and pleasing story than tashan the much hyped and over ? promoted tashan poorly bombed at the box office which it certainly deserved br br in my view this is the worst movie ever made from ? ? raj ? ? how come they handled such a heavy project to new ? ? ? who has no actual sense of making action flick he tried to imitate ? ? ways of making like ? but he suffered at last the action scenes are more like than comics or cartoon movies made for ? the audiences br br the story also loses in its meaning and ? to ? win the ? hearts in most scenes anil kapoor reminds me of southern ? star ? in his body languages and ? expressions i am not a fan of neither saif nor akshay but the award of kareena should have finally gone to ? hand instead of akshay just from the starting point i expected of it but at the end it ? me with the climax truth saif is the main behind the whole adventure while akshay joins in the midst in any movie the final should be judged with the whole characters of the entire story and the award or say reward should be given to the one who deserves credit and tashan loses in this way and unexpectedly failed to become a hit br br ? has nothing new to show off his comedian talent here but still reminds of his previous movies he seriously need to form a new image to his fans that would impress them again and again in between saif did a great job in race and now he returned again in his hilarious nature through this movie but he has fully developed himself in the acting field and last but not the least about kareena she looks really hot with bikini dress of which some complain as she became too lean but i myself don't think so instead she became slim yes slim it is a good factor for a female to attract the major people or say male beside them it is nice that ? son ? appears in the beginning last as young saif i hope now he too will lean forward in target of making acting as his career br br those who like this tashan they are either mentally ? or still want to go back to childhood or say want to be admitted in an asylum thumbs down to ? director ? ? ? who ? the project offered by ? raj films in future he should experiment and study the script minimum of 5 years before going into practical directions br br sorry i don't like to rate good stars to this type of junk movies",
    "true_label": "Negative"
  },
  {
    "text": "? where do i begin i wanted to enjoy this movie and i did still i wanted to be able to enjoy it for being another zombie film that was worth my ? and it ? this was a different kind of enjoyment this was ? a perverse glee that i ? in watching one of the most ridiculous films id seen yet and i dont much care for whatever ? excuses were there was no excuse for this film going how it went this was a bad film all the way around yet i still cant give it below a 4 out of ten which is what i gave it because well at least i was able to laugh at this ? of a movie br br i had to imagine these zombies that were all over the ? of these buildings everywhere had to imagine that they were either bored as hell so they ? up on the ? and ? themselves high on stone ? or they saw the ? living ? band of jerk offs coming around so they took it upon themselves to stage numerous ? ? hell what else is there to do when ? dead br br i had to laugh at some zombies performing what looked to be martial arts ? kicks and jumps and some ? about like traditional ? i ? my eyes on a floating head that was never explained i watched in pure horrific delight as the land they were in the ? was absolutely ? in fog heavy doses of fog and that the ? were as they were ? castle ? i had to even cringe when i saw that the design for a cure for this plague was ? on a ? as an ? with lines ? from each angle with dead one written in the middle i had to ask myself if the science of ? zombies is that easy then i wonder if i could come up with a little something to start a zombie ? here br br all in all the effects were overboard the dubbing horrid im sure the original acting as poor the story absurd the zombies inconsistent even in a bad way they ? all been similar and the women ugly but i found myself enjoying this thing it was a fun watch it turned out to be a very very bad film and i would not recommend this thing unless one is into bad directorial exploitation films but still again i say it was worth a good laugh i ? zombie films no matter what but when this had ? name attached to it it ? been much better let me dare say zombie holocaust was better",
    "true_label": "Negative"
  },
  {
    "text": "? i really must have caught a different film from the rest of the ? on this site because at a screening of the film last night the audience was so ? by the ? that i'm not even kidding half walked out shot as if the filmmaker thought he were approaching some daring new territory by presenting a homosexual coming of age story the film ? david lynch inspired visuals with fassbinder inspired acting the performances in this film are so dull and bored that i figured one of the actors was going to pass out by how uninspired they seemed to be by the script what's worse is that it's colored like an episode of miami vice i don't know who this director thinks he is maybe he has ? of the surreal like ? ? etc but the problem is that all of the ? mentioned directors display a level of ? sensibility that is sorely lacking here i could understand the ? of this film about ten years ago but when we've got masterpieces such as bad ? mysterious skin and show me love why bother with this cinematic turd there is nothing new to be seen here",
    "true_label": "Negative"
  },
  {
    "text": "? tom ? ? br br aspect ratio 1 ? 1 br br sound format ? br br in late 19th century england young tom brown alex ? is sent to the public school at ? where he experiences the ? of a radical new ? stephen ? and stands up to the ? resident bully ? joseph ? br br already the subject of numerous screen adaptations most notably gordon ? superior 1951 version thomas ? ? novel gets the early 21st century treatment courtesy of screenwriter ashley ? tv's where the heart is and director david moore the ? saga it's pleasant enough and watchable but it's also rather ? and dull distinguished only by ? sincere performance as the new principal determined to ? away some of the ? most dubious ? and by the introduction of a possible new star in 14 year old ? a talented kid with the kind of ? charm and vivid good looks that should take him all the way to hollywood and beyond otherwise this is typical uk tv fodder the kind of stuff ? by executives eager to fill the ? with ? product even one as thoroughly ? as this the uk ? ? ? described it as ? odd and raised a ? ? over all of that ? and brutality and a handsome ? villain torturing the life out of sweet young boys quite",
    "true_label": "Negative"
  },
  {
    "text": "? not that much things happen in this movie but a lot of meanings the woman thought she had all that she can in life but that was indeed not true and she found out herself when she met this person who was ? some research for his next job there really should be more types of movies like this im not even that old as considered mature im 13 by the way and i still got the idea and point of the film the main point is in my opinion don't think you can't have a better life just because you currently have this one br br though i got to admit i was thinking of watching another movie but after reading all the reviews and seen the trailer i decided on this one even though i knew not that much action would appear in the film i recommend anyone to watch this movie as it has very good points in the film and is a really good ending",
    "true_label": "Positive"
  },
  {
    "text": "? this movie is wonderful br br i was ? i should say and surprised because of how uniquely it was done the cast the ? the effects everything magnificent i mean it was a love story yes but what made it outstanding from the rest was that it was told in an entertaining wholesome manner br br for me it is the representation of modern fairy tale it's like the modern peter pan simply amazing br br i surely would buy a copy of this the moment it hit the market br br this movie is really a double must see one 10 stars for that",
    "true_label": "Positive"
  },
  {
    "text": "? steve carpenter cannot make horror movies first of all the casting was very wrong for this movie the only decent part was the hot brown haired girl from buffy the vampire ? this movies has no gore usually a key ? to a horror movie no action no acting and no suspense also a key ? wes ? is a good actor but he is so dry and plain in this that it's sad there were a few parts that were supposed to be funny continuing the teen horror comedy movies and no one laughed in the audience i thought that this movie was rated r and i didn't pay attention and realized it had been changed to pg 13 anyway see this movie if you liked i still know what you did last summer that's the only type of person who would find this movie even remotely scary and seriously this is to you steve carpenter stop making horror movies this movie makes scream look like texas chainsaw massacre",
    "true_label": "Negative"
  }
]

def query_ollama(review_text):
    """Sends the prompt to the local Ollama instance."""
    # We create a specific prompt instructing LLaMA to just give the label
    prompt = f"""
    Classify the sentiment of the following movie review as either 'Positive' or 'Negative'.
    Review: "{review_text}"
    
    Answer with only one word: Positive or Negative.
    """
    
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }
    
    try:
        response = requests.post(OLLAMA_URL, json=payload)
        if response.status_code == 200:
            return response.json().get("response", "").strip()
        else:
            return f"Error: {response.status_code}"
    except Exception as e:
        return f"Error: {e}"

# --- MAIN EXECUTION ---
print(f"Starting LLaMA evaluation on {len(test_data)} reviews...")
print("-" * 50)

correct_predictions = 0
total_samples = len(test_data)

for i, item in enumerate(test_data):
    review = item['text']
    true_label = item['true_label']
    
    # Ask LLaMA
    print(f"Processing review {i+1}/{total_samples}...", end=" ")
    llama_response = query_ollama(review)
    
    # Normalize response to handle small variations (e.g., "Positive." vs "positive")
    clean_response = llama_response.lower().replace(".", "")
    
    if "positive" in clean_response:
        pred_label = "Positive"
    elif "negative" in clean_response:
        pred_label = "Negative"
    else:
        pred_label = "Unknown"
        
    # Check match
    is_correct = (pred_label == true_label)
    if is_correct:
        correct_predictions += 1
        
    print(f"[{'CORRECT' if is_correct else 'WRONG'}]")
    print(f"   True: {true_label} | LLaMA: {pred_label}")

print("-" * 50)
final_accuracy = (correct_predictions / total_samples) * 100
print(f"Final LLaMA Accuracy: {final_accuracy:.2f}%")