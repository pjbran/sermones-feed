# Ex Ōre Equī · Sunday 15 November 2026 (a.d. XVII Kal. Dec.). Free voices (Jenny + Paola). English → Latin on every line, then all the Latin again.
# Sources (read 15 Nov 2026, early morning, Canberra): Bureau of Meteorology place pages (Canberra Central, The Rocks, East Melbourne,
# Brisbane City, North Hobart, Berrimah), WillyWeather West Beach (BOM data) · The Nightly 12 Nov (Andrew Greene), PS News 13 Nov,
# Headtopics/The Age 13 Nov, VisaVerge 13 Nov (backpacker visas) · AP via ClickOnDetroit 14 Nov, Gulf News 14 Nov (Iran, Hormuz, Shenzhen) ·
# NPR via KUNR 14 Nov, Deseret News 14 Nov (Hegseth) · Kyiv Post 13 Nov, RTÉ 14 Nov, Euromaidan Press 13 Nov, Latin Times (Ukraine) ·
# CBS News/AP via Yahoo 12 Nov (William found near Walhalla) · The Spectator Australia, Flat White 14 Nov (Michael de Percy) ·
# Wikipedia, Albertus Magnus.
import json
L = []
def en(t): L.append(['en', t])
def la(t): L.append(['la', t])
def sec(t): L.append(['sec', t])
def p1(t): L.append(['p1', t])
def pl(e, t): L.append(['pl', e, t])
def spl(e, t): L.append(['spl', e, t])
def p1pl(e, t): L.append(['p1pl', e, t])

# ---------------- opening ----------------
spl("Hello, listeners. This is Straight from the Horse's Mouth.", "Salvēte, audītōrēs. Haec sunt nūntia ex ōre equī.")
pl("Today is Sunday, the seventeenth day before the Kalends of December.", "Hodiē est diēs Sōlis, ante diem septimum decimum Kalendās Decembrēs.")
pl("In the year 2026.", "Annō bis mīllēsimō vīcēsimō sextō.")
pl("Sunday: the day of the sun. Today the sun is shy.", "Diēs Sōlis. Sed hodiē sōl timidus est.")
pl("First, the weather. Then Australian affairs.", "Prīmum tempestās. Deinde rēs Austrāliae.")
pl("Then the world: Iran, America, Ukraine.", "Deinde orbis terrārum: Īrānia, America, Ūcraīna.")
pl("Then a happy story, opinion, and today in history.", "Tum rēs laeta, opīniō, et hodiē in historiā.")
pl("At the end, the words of the day.", "In fīne, verba diēī.")

# ---------------- weather ----------------
en("The weather. Canberra: 25 degrees, partly cloudy, a 70% chance of rain, perhaps a thunderstorm in the afternoon. Tomorrow cooler: 19, cloudy.")
spl("The weather.", "Tempestās.")
pl("First, Canberra.", "Prīmum Canberra.")
pl("Yesterday we said: tomorrow showers are likely, and perhaps thunder in the afternoon.", "Herī dīximus: crās imbrēs probābilēs sunt, et post merīdiem fortasse tonitrus.")
pl("And so it is. Today in Canberra the sky is partly cloudy.", "Et ita est. Hodiē Canberrae caelum partim nūbilum est.")
pl("In the morning 12 degrees.", "Māne duodecim gradūs.")
pl("In the afternoon 25 degrees.", "Post merīdiem vīgintī quīnque gradūs.")
pl("Rain is likely: 70 per cent. In the afternoon, perhaps thunder.", "Pluvia probābilis est: septuāgintā per centum. Post merīdiem fortasse tonitrus.")
pl("Tomorrow, Monday, it is cooler. The sky is cloudy, and perhaps rain.", "Crās, diē Lūnae, frīgidius est. Caelum nūbilum est, et fortasse pluvia.")
pl("Tomorrow morning 9 degrees, in the afternoon 19.", "Crās māne novem gradūs, post merīdiem ūndēvīgintī.")
pl("Now the other cities.", "Nunc cēterae urbēs.")
pl("In Sydney showers, perhaps thunder. 22 degrees.", "Sydnēiae imbrēs, fortasse tonitrus. Vīgintī duo gradūs.")
pl("In Melbourne showers. 17 degrees.", "Melburnī imbrēs. Septendecim gradūs.")
pl("In Brisbane thunder is likely, perhaps severe. 31 degrees.", "Brisbanae tonitrus probābilis est, fortasse gravis. Ūnus et trīgintā gradūs.")
pl("In Adelaide a shower or two. 19 degrees.", "Adēlāidae ūnus aut alter imber. Ūndēvīgintī gradūs.")
pl("In Hobart showers. 15 degrees.", "Hobartī imbrēs. Quīndecim gradūs.")
pl("In Darwin thunder is likely. 34 degrees.", "Darwīnī tonitrus probābilis est. Quattuor et trīgintā gradūs.")
pl("About Perth we have no new report today.", "Dē Perthā hodiē nūntium novum nōn habēmus.")
pl("Showers almost everywhere. Good for the grass.", "Imbrēs ferē ubīque. Bonum herbae.")
pl("That is the weather.", "Haec est tempestās.")

# ---------------- Australia ----------------
en("Australia. The backpacker backdown is coming. Tony Burke: 'I am completely open to that.' The cap on third-year visas is expected to rise by 20,000. The Nightly calls it yet another Albanese government capitulation.")
spl("Australian affairs.", "Rēs Austrāliae.")
pl("Yesterday we said: the Government is considering a retreat on the backpackers.", "Herī dīximus: rēs pūblica dē receptū dē viātōribus cōgitat.")
pl("Backpackers are young travellers. They come to Australia and they work on farms.", "Viātōrēs sunt iuvenēs peregrīnī. In Austrāliam veniunt et in agrīs labōrant.")
pl("The visas for a third year: down from 31,000 to only 5,000.", "Licentiae annī tertiī: ab ūnō et trīgintā mīlibus ad quīnque mīlia tantum.")
pl("Then came the outcry, from the farmers and from the innkeepers.", "Tum clāmor ortus est, ab agricolīs et ā caupōnibus.")
pl("Today the retreat is near.", "Hodiē receptus prope est.")
pl("Burke was asked about a change. Burke said: I am completely open to that.", "Burke dē mūtātiōne rogātus est. Burke dīxit: omnīnō apertus sum.")
pl("But Burke also says: we are not quite at a landing place yet.", "Sed Burke etiam dīcit: nōndum omnīnō ad locum dēscēnsūs pervēnimus.")
pl("A landing place. Every horse knows the landing place: just after the fence.", "Locus dēscēnsūs. Omnis equus locum dēscēnsūs nōvit: statim post saepem.")
pl("The Nightly says: the visas for a third year will perhaps go up by 20,000: to 25,000.", "The Nightly dīcit: licentiae annī tertiī fortasse vīgintī mīlibus augēbuntur: ad vīgintī quīnque mīlia.")
pl("But Burke says: the total numbers I could not compromise on.", "Sed Burke dīcit: dē summā numerōrum cēdere nōn potuī.")
pl("The new rules are expected within weeks.", "Novae rēgulae intrā paucās hebdomadēs exspectantur.")
pl("Why the hurry? The busy summer is coming.", "Cūr festīnātiō? Aestās negōtiōsa venit.")
pl("The Nightly calls it yet another retreat of the Albanese government.", "The Nightly id vocat etiam alium receptum reī pūblicae Albanese.")
pl("And this week the government also retreated on the sale of old military sites in Sydney and Melbourne.", "Et hāc hebdomade rēs pūblica etiam dē venditiōne veterum locōrum mīlitārium Sydnēiae et Melburnī sē recēpit.")
pl("Retreat on the backpackers, retreat on the sites. The government's favourite direction is backwards.", "Receptus dē viātōribus, receptus dē locīs. Via dīlēcta reī pūblicae est retrōrsum.")
pl("But the fruit must be picked, and the hay must be brought in.", "Sed pōma carpenda sunt, et faenum condendum est.")
pl("That is the state of Australia today.", "Haec est rēs Austrāliae hodiē.")

# ---------------- world 1: Iran ----------------
en("The world. Trump is weighing holding off on further attacks on Iran unless Tehran or the Houthis make new provocations. Rubio: the economic pain is so great. Iran at the UN: it never closed the door to diplomacy, but threatens an immediate and decisive response.")
spl("The world.", "Orbis terrārum.")
pl("First, Iran.", "Prīmum Īrānia.")
pl("Yesterday we said: Iran says: no talks about inspections, while threats remain.", "Herī dīximus: Īrānia dīcit: nūllī sermōnēs dē īnspectiōnibus, dum minae manent.")
pl("And Iran says: we have destroyed an American radar. America says: no damage.", "Et Īrānia dīcit: speculātōrium Americānum dēlēvimus. America dīcit: nūllum damnum.")
pl("Today: Trump is considering holding back from new attacks on Iran.", "Hodiē: Trump cōgitat ā novīs impetibus in Īrāniam abstinēre.")
pl("Unless Iran, or the Houthis of Yemen, start new trouble.", "Nisi Īrānia, aut Hūthī Yemeniae, nova incitāmenta faciant.")
pl("He has not yet decided.", "Nōndum dēcrēvit.")
pl("Rubio says: the economic pain that we are inflicting on that regime is so great.", "Rubio dīcit: dolor oeconomicus quem illī rēgnō īnferimus tantus est.")
pl("At the United Nations, Iran says: Iran has never closed the door to diplomacy.", "In Nātiōnibus Ūnītīs Īrānia dīcit: Īrānia ostium diplōmatiae numquam clausit.")
pl("But if America or Israel bomb again: a sudden and decisive response.", "Sed sī America aut Isrāēl iterum bombīs pulsābunt: respōnsum subitum et dēcrētōrium.")
pl("The door is open, says Iran. But behind the door there is a stick.", "Ostium apertum est, dīcit Īrānia. Sed post ostium baculum est.")
pl("In the stable we prefer a door with a carrot behind it.", "In stabulō ostium mālumus post quod carōta est.")
pl("And the Revolutionary Guards say: two oil ships have burned in the Strait of Hormuz.", "Et Custōdēs Revolūtiōnis dīcunt: duae nāvēs oleāriae in fretō Hormuziānō ārsērunt.")
pl("Iran does not name the ships. No one has confirmed it.", "Īrānia nāvēs nōn nōminat. Nēmō id cōnfirmāvit.")
pl("And on Thursday, Trump will meet Xi and Putin, in the city of Shenzhen in China. Iran will be on the table.", "Et diē Iovis Trump cum Xi et Putin conveniet, in urbe Shenzhen in Sīnīs. Īrānia in mēnsā erit.")
pl("No attacks for now, the door open, a stick behind the door, and the Strait still shut.", "Nūllī impetūs nunc, ostium apertum, baculum post ostium, et fretum adhūc clausum.")

# ---------------- world 2: US ----------------
en("America. Hegseth's historically strange week: the failed impeachment, the Tomb rebuke, the medal. Trump: the Democrats' attempt 'has miserably failed'. Democrat Melanie Stansbury: 'This is not the end.'")
pl("Now the United States of America.", "Nunc Cīvitātēs Foederātae Americae.")
pl("Yesterday we said: American soldiers perhaps in Poland, for good.", "Herī dīximus: mīlitēs Americānī fortasse in perpetuum in Polōniā.")
pl("Today the Deseret News looks back on a strange week for Hegseth, the Secretary of War.", "Hodiē ephēmeris Deseret hebdomadem mīram Hegseth, ministrī bellī, respiciunt.")
pl("On Tuesday the House of Representatives sent the charges against Hegseth back to a committee. 211 against 204.", "Diē Martis Domus Repraesentantium crīmina contrā Hegseth ad commissiōnem remīsit. Ducenta ūndecim contrā ducenta quattuor.")
pl("Seven votes. Almost a photo finish, as on the racecourse.", "Septem suffrāgia. Paene pār fīnis, ut in curriculō.")
pl("But the Democrat Melanie Stansbury says: this is not the end. We will bring back the charges.", "Sed Dēmocrata Melanie Stansbury dīcit: hic nōn est fīnis. Crīmina reportābimus.")
pl("On Wednesday, at the Tomb of the Unknown Soldier, a guard called for silence.", "Diē Mercuriī, ad sepulcrum Mīlitis Ignōtī, custōs silentium postulāvit.")
pl("On Thursday Hegseth gave a soldier a medal. Well done, Specialist.", "Diē Iovis Hegseth mīlitī īnsigne dedit. Bene fēcistī, mīles.")
pl("Charges, silence, a medal. In one week. Most of us manage one of these a year.", "Crīmina, silentium, īnsigne. Ūnā hebdomade. Plērīque ūnum ex hīs quotannīs efficimus.")

# ---------------- world 3: Ukraine ----------------
en("Ukraine. Zelensky: an exchange of 1,200 to 1,300 prisoners from each side, the largest of the war. Three to five Europeans at the next talks. Zelensky says the Americans asked: if Ukraine joins NATO, would it withdraw from the Donbas? Russia refuses to discuss sparing the power grid.")
pl("Now Ukraine.", "Nunc Ūcraīna.")
pl("Yesterday we said: Zelensky met Witkoff and Kushner near Dublin.", "Herī dīximus: Zelensky cum Witkoff et Kushner prope urbem Dublin convēnit.")
pl("And Zelensky says: our soldiers will come home.", "Et Zelensky dīcit: mīlitēs nostrī domum redībunt.")
pl("Today we have the number. Zelensky says: 1,200 or 1,300 prisoners, from each side.", "Hodiē numerum habēmus. Zelensky dīcit: mīlle ducentī aut mīlle trecentī captīvī, ab utrāque parte.")
pl("It will be the biggest exchange of prisoners of the whole war.", "Erit maxima permūtātiō captīvōrum tōtīus bellī.")
pl("And at the next talks, three to five Europeans will sit at the table.", "Et in proximīs sermōnibus trēs ad quīnque Eurōpaeī ad mēnsam sedēbunt.")
pl("Then a new chapter. Zelensky says: the Americans raised a question.", "Tum novum caput. Zelensky dīcit: Americānī quaestiōnem mōvērunt.")
pl("What if Ukraine joins NATO? Would Ukraine withdraw from the Donbas?", "Quid sī Ūcraīna in NATO intrābit? Ūcraīnane ē Donbassō recēdet?")
pl("Zelensky says: this has happened for the first time. And he will ask the Ukrainian people.", "Zelensky dīcit: hoc prīmum factum est. Et populum Ūcraīnum rogābit.")
pl("But about electricity, Russia will not talk. Russia wants to keep striking, says Zelensky.", "Sed dē ēlectricitāte Russia loquī nōn vult. Russia ferīre pergere vult, dīcit Zelensky.")
pl("Russia has struck energy sites more than 310 times since the start of November.", "Russia loca energiae plūs quam trecentiēs deciēs percussit, ab initiō mēnsis Novembris.")
pl("Ukraine in the dark, and winter is coming. In a cold stable, we stand closer together.", "Ūcraīna in tenebrīs, et hiems venit. In stabulō frīgidō propius stāmus.")
pl("A great exchange of prisoners, Europeans at the table, a question about NATO, and still no peace.", "Magna permūtātiō captīvōrum, Eurōpaeī ad mēnsam, quaestiō dē NATO, et adhūc nūlla pāx.")

# ---------------- good news ----------------
en("Something good. William, 17, was lost for six days in the bush near Walhalla in Victoria. A police helicopter found him on a rock by a creek. His mother: 'I'm just over the moon that he's alive.'")
spl("Good news.", "Rēs laeta.")
pl("William is seventeen years old. He went camping with a friend in Victoria.", "Gulielmus septendecim annōs nātus est. Cum amīcō in Victōriā castra posuit.")
pl("The place is near Walhalla, an old town of gold, about 185 kilometres east of Melbourne.", "Locus prope Walhallam est, oppidum vetus aurī, circiter centum octōgintā quīnque chiliometra ad orientem Melburnī.")
pl("William got lost in the bush. For six days he was lost.", "Gulielmus in silvā errāvit. Sex diēs āmissus erat.")
pl("More than a hundred people searched for him.", "Plūs quam centum hominēs eum quaesīvērunt.")
pl("On Thursday a police helicopter found him, on a rock beside a stream, two kilometres from the camp.", "Diē Iovis helicoptērum vigilum eum invēnit, in saxō prope rīvum, duo chiliometra ā castrīs.")
pl("William woke at the sound of the helicopter, and gave a thumbs up.", "Gulielmus ad sonum helicoptērī experrēctus est, et pollicem sustulit.")
pl("The helicopter lifted him to safety. He was in good spirits.", "Helicoptērum eum in tūtum sustulit. Bonō animō erat.")
pl("His mother says: I'm just over the moon that he's alive.", "Māter eius dīcit: super lūnam sum, quod vīvit.")
pl("And she says: he is grounded for life. He is not going anywhere ever again.", "Et dīcit: domī manēbit in perpetuum. Numquam iterum quōquam ībit.")
pl("Grounded for life. In the stable we call that a normal week. There is hay.", "Domī in perpetuum. In stabulō hoc hebdomadem solitam vocāmus. Faenum est.")

# ---------------- opinion ----------------
en("Opinion. This is the view of Michael de Percy, in The Spectator Australia: 'Silence on coal, hubris at COP31.' Albanese and Bowen 'do statesmanship through other people's money'.")
spl("Opinion.", "Opīniō.")
pl("This is the view of Michael de Percy, in The Spectator Australia.", "Haec est sententia Michaelis de Percy, in Spectātōre Austrāliae.")
pl("Yesterday we said: Bowen is at the great conference on the climate.", "Herī dīximus: Bowen in magnō conventū dē climate est.")
pl("De Percy says: in his speech, Albanese did not say the word coal. Not once.", "De Percy dīcit: in ōrātiōne suā Albanese verbum carbō nōn dīxit. Nē semel quidem.")
pl("No coal, no gas, no oil. Only the sun, batteries, and the Pacific.", "Nūllus carbō, nūllum gas, nūllum oleum. Sōlum sōl, batteriae, et Pacificus.")
pl("Why? De Percy says: at home the word coal takes away votes.", "Cūr? De Percy dīcit: domī verbum carbō suffrāgia aufert.")
pl("A speech on energy without the word coal. A speech on horses without the word hay. Impossible. And yet.", "Ōrātiō dē energiā sine verbō carbō. Ōrātiō dē equīs sine verbō faenum. Fierī nōn potest. Et tamen.")
pl("De Percy says: nuclear power is the proven way to replace coal. Albanese and Bowen did not speak of it.", "De Percy dīcit: vīs nucleāris via probāta est ad carbōnem substituendum. Albanese et Bowen dē eā nōn locūtī sunt.")
pl("De Percy writes: Albanese and Bowen do statesmanship with other people's money.", "De Percy scrībit: Albanese et Bowen rem pūblicam gerunt pecūniā aliēnā.")
pl("That is the opinion of Michael de Percy.", "Haec est opīniō Michaelis de Percy.")

# ---------------- on this day ----------------
en("On this day in 1280 Saint Albert the Great died in Cologne. A German Dominican, the 'universal doctor', teacher of Thomas Aquinas. As bishop of Regensburg he refused to ride a horse and walked everywhere.")
spl("Today in history.", "Hodiē in historiā.")
pl("Today, in the year 1280, Saint Albert the Great died, in Cologne, in Germany.", "Hodiē, annō mīllēsimō ducentēsimō octōgēsimō, sānctus Albertus Magnus mortuus est, Colōniae, in Germāniā.")
pl("He was a German, a Dominican friar, and a very learned man.", "Germānus erat, frāter Dominicānus, et vir doctissimus.")
pl("They called him the universal doctor. He wrote about everything: plants, animals, stones, stars.", "Eum doctōrem ūniversālem vocābant. Dē omnibus scrīpsit: dē herbīs, dē animālibus, dē lapidibus, dē stēllīs.")
pl("In Paris his student was Thomas Aquinas.", "Lutētiae discipulus eius erat Thomās Aquīnās.")
pl("He was bishop of Regensburg. But he would not ride a horse. He walked the whole diocese on foot.", "Episcopus Ratisbonae erat. Sed equō vehī nōluit. Tōtam dioecēsim pedibus ambulāvit.")
pl("He would not ride a horse. We have read this three times. We forgive him. Slowly.", "Equō vehī nōluit. Hoc ter lēgimus. Eī ignōscimus. Lentē.")
pl("In 1931 he was made a saint and a Doctor of the Church. He is patron of the natural scientists.", "Annō mīllēsimō nōngentēsimō trīcēsimō prīmō sānctus et Doctor Ecclēsiae factus est. Patrōnus est physicōrum.")
pl("Marcus and Lucius, as always, were there. But that is another story.", "Mārcus et Lūcius, ut semper, aderant. Sed id alia fābula est.")

# ---------------- summary ----------------
en("The day in brief.")
spl("Summary of the news.", "Summa rērum.")
pl("In Canberra today 25 degrees, rain likely, and perhaps thunder. Tomorrow cooler.", "Canberrae hodiē vīgintī quīnque gradūs, pluvia probābilis, et fortasse tonitrus. Crās frīgidius.")
pl("The retreat on the backpackers is near. Burke says: I am completely open to that.", "Receptus dē viātōribus prope est. Burke dīcit: omnīnō apertus sum.")
pl("The visas for a third year will perhaps go up to 25,000.", "Licentiae annī tertiī fortasse ad vīgintī quīnque mīlia augēbuntur.")
pl("Trump is considering holding back from new attacks on Iran.", "Trump cōgitat ā novīs impetibus in Īrāniam abstinēre.")
pl("Iran says: Iran has never closed the door to diplomacy.", "Īrānia dīcit: Īrānia ostium diplōmatiae numquam clausit.")
pl("On Thursday Trump will meet Xi and Putin in China.", "Diē Iovis Trump cum Xi et Putin in Sīnīs conveniet.")
pl("A strange week for the Secretary of War: charges, silence, a medal.", "Hebdomas mīra ministrō bellī: crīmina, silentium, īnsigne.")
pl("The biggest exchange of prisoners: 1,200 or 1,300 from each side.", "Maxima permūtātiō captīvōrum: mīlle ducentī aut mīlle trecentī ab utrāque parte.")
pl("Three to five Europeans will sit at the table.", "Trēs ad quīnque Eurōpaeī ad mēnsam sedēbunt.")
pl("A helicopter found William, after six days in the bush.", "Helicoptērum Gulielmum invēnit, post sex diēs in silvā.")
pl("De Percy says: in his speech Albanese did not say the word coal.", "De Percy dīcit: in ōrātiōne suā Albanese verbum carbō nōn dīxit.")
pl("Albert the Great died on this day, in the year 1280.", "Albertus Magnus hōc diē mortuus est, annō mīllēsimō ducentēsimō octōgēsimō.")

# ---------------- words of the day ----------------
en("The words of the day. Five sentences, slowly.")
spl("The words of the day.", "Verba diēī.")
pl("The retreat is near.", "Receptus prope est.")
pl("Iran has never closed the door to diplomacy.", "Īrānia ostium diplōmatiae numquam clausit.")
pl("Trump is considering holding back from new attacks.", "Trump cōgitat ā novīs impetibus abstinēre.")
pl("A helicopter found him, in the bush.", "Helicoptērum eum invēnit, in silvā.")
pl("He would not ride a horse.", "Equō vehī nōluit.")
pl("Again.", "Iterum.")
pl("The retreat is near.", "Receptus prope est.")
pl("Iran has never closed the door to diplomacy.", "Īrānia ostium diplōmatiae numquam clausit.")
pl("Trump is considering holding back from new attacks.", "Trump cōgitat ā novīs impetibus abstinēre.")
pl("A helicopter found him, in the bush.", "Helicoptērum eum invēnit, in silvā.")
pl("He would not ride a horse.", "Equō vehī nōluit.")
pl("That was the news, straight from the horse's mouth. Goodbye, listeners. Again tomorrow.", "Haec fuērunt nūntia ex ōre equī. Valēte, audītōrēs. Crās iterum.")
p1pl("Now everything again, in Latin only.", "Nunc omnia iterum, Latīnē tantum.")

job = {
 "type": "news", "date": "2026-11-15", "music": "v5",
 "title": "Ex Ōre Equī · Diēs Sōlis, a.d. XVII Kal. Dec. (Sun 15 Nov 2026)",
 "summary": ("Canberra: 12–25°, partly cloudy, 70% chance of rain, possible afternoon thunderstorm, NW 15–25 km/h turning E; Monday 9–19°, cloudy. "
             "Sydney 22, Melbourne 17, Brisbane 31 (storms), Adelaide 19, Hobart 15, Darwin 34. "
             "Australia: the backpacker backdown nears: Burke 'I am completely open to that', 'We are not quite at a landing place yet', total numbers "
             "'something that I could not compromise on'; The Nightly: third-year cap (5,000) expected to rise by 20,000, 'yet another' capitulation; "
             "ballot may be delayed; British backpackers 47,238 → 79,412; govt also walked back selling defence heritage sites. "
             "Iran: Trump weighs holding off on new attacks unless Tehran or the Houthis provoke; Rubio: 'The economic pain that we are inflicting on "
             "that regime is so great'; Iran at the UN (Darzi): 'never closed the door to diplomacy', warns of 'an immediate and decisive response'; "
             "IRGC claims two tankers burned in Hormuz (unverified); Trump meets Xi and Putin in Shenzhen on Thursday. "
             "US: Hegseth's strange week: House 211–204 to refer impeachment articles, 11 Democrats absent; Trump: 'miserably failed'; Stansbury: "
             "'This is not the end'; Tomb sentinel; medal. Ukraine: exchange of 1,200–1,300 POWs each side, the war's largest; 3–5 Europeans at the "
             "next talks; Zelensky: the US asked 'What if Ukraine joins NATO? Would Ukraine withdraw from Donbas?'; Russia won't discuss sparing the grid, "
             "310+ energy strikes since 1 Nov. Good news: William, 17, found alive after six days lost near Walhalla. Opīniō: Michael de Percy, "
             "'Silence on coal, hubris at Cop31' (Spectator Australia). St Albert the Great died 15 Nov 1280. Every line in English, then Latin; "
             "then all the Latin again. Sources: Bureau of Meteorology; WillyWeather; The Nightly; PS News; The Age via Headtopics; VisaVerge; AP; "
             "Gulf News; NPR; Deseret News; Kyiv Post; RTÉ; Euromaidan Press; Latin Times; CBS News/AP; The Spectator Australia; Wikipedia."),
 "lines": L,
}
if __name__ == "__main__":
    json.dump(job, open("jobs/0077-news-2026-11-15.json", "w"), ensure_ascii=False, indent=1)
    lat = [r[-1] for k, *r in L if k != 'en']
    w = sum(len(t.split()) for t in lat)
    import re
    bad = [t for t in lat if re.search(r'\d', t)]
    print(len(L), 'lines ·', len(lat), 'Latin lines ·', w, 'Latin words · digits:', bad)
