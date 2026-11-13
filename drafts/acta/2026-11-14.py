# Ex Ōre Equī · Saturday 14 November 2026 (a.d. XVIII Kal. Dec.). Free voices (Jenny + Paola). English → Latin on every line, then all the Latin again.
# Sources (read 14 Nov 2026, early morning, Canberra): Bureau of Meteorology, Canberra Central forecast (issued 13 Nov 8:28 am) ·
# ABC News federal politics blog 13 Nov (backpacker visas, citing The Australian; Bowen at COP31; Grattan) · Fox News live blog 13 Nov,
# Jerusalem Post 13 Nov, Democracy Now 13 Nov, Just Security Early Edition 13 Nov (Iran, IAEA, radar in Bahrain, tankers, oil, Bessent,
# Poland, Iglesias medal) · TheJournal.ie, Irish Times/PA, Kyiv Independent 12 Nov (Zelensky meets Witkoff and Kushner at Baldonnel) ·
# Only Good News Daily 13 Nov (Tricia Johnson) · The Spectator Australia leader "Dismissal 2.0" · Christian History Institute, History Today (Justinian).
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
pl("Today is Saturday, the eighteenth day before the Kalends of December.", "Hodiē est diēs Sāturnī, ante diem duodēvīcēsimum Kalendās Decembrēs.")
pl("In the year 2026.", "Annō bis mīllēsimō vīcēsimō sextō.")
pl("Saturday: a day of rest. Not for the news. Not for the one who reads them.", "Diēs Sāturnī: diēs quiētis. Nōn nūntiīs. Nōn eī quī ea legit.")
pl("First, the weather. Then Australian affairs.", "Prīmum tempestās. Deinde rēs Austrāliae.")
pl("Then the world: Iran, America, Ukraine.", "Deinde orbis terrārum: Īrānia, America, Ūcraīna.")
pl("Then a happy story, opinion, and today in history.", "Tum rēs laeta, opīniō, et hodiē in historiā.")
pl("At the end, the words of the day.", "In fīne, verba diēī.")

# ---------------- weather ----------------
en("The weather. Canberra: 28 degrees, showers very likely, perhaps a thunderstorm in the afternoon. Tomorrow 27 and more showers.")
spl("The weather.", "Tempestās.")
pl("First, Canberra.", "Prīmum Canberra.")
pl("Yesterday we said: tomorrow showers are likely, and perhaps thunder again.", "Herī dīximus: crās imbrēs probābilēs sunt, et fortasse iterum tonitrus.")
pl("And so it is. Today in Canberra the sky is partly cloudy.", "Et ita est. Hodiē Canberrae caelum partim nūbilum est.")
pl("In the morning 13 degrees.", "Māne trēdecim gradūs.")
pl("In the afternoon it is warm: 28 degrees.", "Post merīdiem calidum est: duodētrīgintā gradūs.")
pl("Showers are very likely. In the afternoon and early evening, perhaps thunder.", "Imbrēs valdē probābilēs sunt. Post merīdiem et prīmā vesperā, fortasse tonitrus.")
pl("The wind blows from the north-west, 15 to 25 kilometres an hour.", "Ventus ab occidente et septentriōne flat, quīndecim ad vīgintī quīnque chiliometra in hōrā.")
pl("When there is thunder, a wise animal stays in the stable.", "Ubi tonitrus est, sapiēns animal in stabulō manet.")
pl("Tomorrow, Sunday, showers are likely, mostly in the morning, and perhaps thunder in the afternoon.", "Crās, diē Sōlis, imbrēs probābilēs sunt, māxime māne, et post merīdiem fortasse tonitrus.")
pl("Tomorrow morning 13 degrees, in the afternoon 27.", "Crās māne trēdecim gradūs, post merīdiem septem et vīgintī.")
pl("About the other cities we have no new report today.", "Dē cēterīs urbibus hodiē nūntium novum nōn habēmus.")
pl("Our messenger rode out to the other cities. He has not yet returned.", "Nūntius noster ad cēterās urbēs equitāvit. Nōndum rediit.")
pl("Perhaps he found good grass. We do not blame him.", "Fortasse herbam bonam invēnit. Eum nōn culpāmus.")
pl("That is the weather.", "Haec est tempestās.")

# ---------------- Australia ----------------
en("Australia. Two months after announcing cuts to backpacker visas, the Government is considering a backdown after an outcry from farmers and hospitality.")
spl("Australian affairs.", "Rēs Austrāliae.")
pl("Yesterday we said: the price of electricity could nearly double.", "Herī dīximus: pretium ēlectricitātis paene duplicārī potest.")
pl("And Albanese was in Turkey, at the great conference on the climate.", "Et Albanese in Turciā erat, in magnō conventū dē climate.")
pl("Today the minister Chris Bowen is at the conference. He pushes a practical deal, under pressure over fossil fuels.", "Hodiē minister Chris Bowen in conventū est. Pactiōnem prūdentem petit, sub pressūrā dē combustibilibus fossilibus.")
pl("But at home there is a new story: the backpackers.", "Sed domī nova fābula est: viātōrēs.")
pl("Backpackers are young travellers. They come to Australia and they work on farms.", "Viātōrēs sunt iuvenēs peregrīnī. In Austrāliam veniunt et in agrīs labōrant.")
pl("Two months ago the minister Tony Burke announced cuts to backpacker visas.", "Ante duōs mēnsēs minister Tony Burke licentiās viātōrum minuendās nūntiāvit.")
pl("Labor wants to bring migration down to 225,000, by the year 2028.", "Labōrānī migrātiōnem ad ducenta vīgintī quīnque mīlia redūcere volunt, usque ad annum bis mīllēsimum vīcēsimum octāvum.")
pl("The visas for a second year: down from 57,000 to 45,000.", "Licentiae annī secundī: ā quīnquāgintā septem mīlibus ad quadrāgintā quīnque mīlia.")
pl("The visas for a third year: down from 31,000 to only 5,000.", "Licentiae annī tertiī: ab ūnō et trīgintā mīlibus ad quīnque mīlia tantum.")
pl("And a ballot: the visas will be given by lot.", "Et sortītiō: licentiae sorte dabuntur.")
pl("Then came the outcry, from the farmers and from the innkeepers.", "Tum clāmor ortus est, ab agricolīs et ā caupōnibus.")
pl("Who will pick the fruit? Who will pour the beer?", "Quis pōma carpet? Quis cervēsiam fundet?")
pl("And who will bring in the hay? We ask for a friend.", "Et quis faenum condet? Prō amīcō rogāmus.")
pl("Now the Government is considering a retreat.", "Nunc rēs pūblica dē receptū cōgitat.")
pl("The Australian says: perhaps the ballot will wait until next year.", "The Australian dīcit: fortasse sortītiō in annum proximum differētur.")
pl("And perhaps the third-year visas will go up to 25,000.", "Et fortasse licentiae annī tertiī ad vīgintī quīnque mīlia augēbuntur.")
pl("Burke says: those conversations are continuing.", "Burke dīcit: illī sermōnēs pergunt.")
pl("Cuts, then a retreat. On the racecourse this is called running the wrong way. The horses on the track were astonished.", "Prīmum minūtiō, deinde receptus. In curriculō hoc vocātur contrā currere. Equī in curriculō obstupuērunt.")
pl("Michelle Grattan writes in The Conversation: the government is in trouble.", "Michelle Grattan in The Conversation scrībit: rēs pūblica in angustiīs est.")
pl("Electricity dear, hay dear, and now a retreat on the backpackers.", "Ēlectricitās cāra, faenum cārum, et nunc receptus dē viātōribus.")
pl("That is the state of Australia today.", "Haec est rēs Austrāliae hodiē.")

# ---------------- world 1: Iran ----------------
en("The world. Iran tells the UN nuclear agency that talks on inspections cannot go ahead under American threats. Iran's Guards claim to have hit a US radar in Bahrain; the Americans say nothing was damaged.")
spl("The world.", "Orbis terrārum.")
pl("First, Iran.", "Prīmum Īrānia.")
pl("Yesterday we said: Trump says: we don't need a deal with Iran.", "Herī dīximus: Trump dīcit: pactiōne cum Īrāniā nōn egēmus.")
pl("And Iran says: the Strait of Hormuz will not open.", "Et Īrānia dīcit: fretum Hormuziānum nōn aperiētur.")
pl("Today Iran has told the nuclear agency of the United Nations: no talks about inspections.", "Hodiē Īrānia agentiae nucleārī Nātiōnum Ūnītārum dīxit: nūllī sermōnēs dē īnspectiōnibus.")
pl("Not while threats remain. Iran speaks of persistent, explicit and public threats by the President.", "Nōn, dum minae manent. Īrānia dē minīs assiduīs, apertīs, et pūblicīs praesidis loquitur.")
pl("And Trump? In an interview he was asked: would you hesitate to use force against Iran?", "Et Trump? In colloquiō rogātus est: dubitārēsne vim contrā Īrāniam adhibēre?")
pl("Trump said: No, without hesitation.", "Trump dīxit: Minimē, sine dubitātiōne.")
pl("And Trump says: the regime in Iran is on the brink of collapse.", "Et Trump dīcit: rēgnum Īrāniae prope ruīnam est.")
pl("Then the Revolutionary Guards of Iran said: we have destroyed an American radar in Bahrain.", "Deinde Custōdēs Revolūtiōnis Īrāniae dīxērunt: speculātōrium Americānum in Bahrainiā dēlēvimus.")
pl("Why? In return for an American strike on a telecommunications tower in the south of Iran.", "Cūr? Prō ictū Americānō in turrem nūntiōrum in merīdiē Īrāniae.")
pl("But the Americans say: we shot down two drones. No injuries, no damage.", "Sed Americānī dīcunt: duōs fūcōs dēiēcimus. Nūllī vulnerātī, nūllum damnum.")
pl("Iran says: the radar is destroyed. America says: no damage. So the radar is not even scratched.", "Īrānia dīcit: speculātōrium dēlētum est. America dīcit: nūllum damnum. Speculātōrium ergō nē rāsum quidem est.")
pl("We sent a horse to count the pieces. He has counted zero pieces. He is still counting.", "Equum mīsimus quī frūsta numeret. Nūlla frūsta numerāvit. Adhūc numerat.")
pl("And in the Strait of Hormuz, oil ships have been hit again: four on Thursday alone.", "Et in fretō Hormuziānō nāvēs oleāriae iterum ictae sunt: quattuor diē Iovis sōlō.")
pl("Yet the price of oil fell this week: a barrel of Brent costs about 96 dollars.", "Tamen pretium oleī hāc hebdomade cecidit: dōlium Brent circiter nōnāgintā sex dollarīs cōnstat.")
pl("The minister Bessent has moved to a military base, because of threats from Iran.", "Minister Bessent in castra migrāvit, propter minās Īrāniae.")
pl("Threats, inspections refused, a radar perhaps destroyed. The Strait still shut.", "Minae, īnspectiōnēs negātae, speculātōrium fortasse dēlētum. Fretum adhūc clausum.")

# ---------------- world 2: US ----------------
en("America. Poland's defence minister met Hegseth and says the Pentagon has given the green light to a permanent US troop presence in Poland. The White House decides at the start of December.")
pl("Now the United States of America.", "Nunc Cīvitātēs Foederātae Americae.")
pl("Yesterday we said: at the Tomb of the Unknown Soldier a guard called for silence.", "Herī dīximus: ad sepulcrum Mīlitis Ignōtī custōs silentium postulāvit.")
pl("Hegseth gave the soldier a medal.", "Hegseth mīlitī īnsigne dedit.")
pl("Hegseth wrote: We love soldiers. We love standards. Well done, Specialist.", "Hegseth scrīpsit: Mīlitēs amāmus. Disciplīnam amāmus. Bene fēcistī, mīles.")
pl("Today a new chapter: Hegseth and Poland.", "Hodiē novum caput: Hegseth et Polōnia.")
pl("On Wednesday the Polish minister of defence, Kosiniak-Kamysz, met Hegseth, the Secretary of War.", "Diē Mercuriī minister dēfēnsiōnis Polōniae, Kosiniak-Kamysz, cum Hegseth, ministrō bellī, convēnit.")
pl("The Polish minister says: the permanent presence of American troops in Poland has been given the green light by the Pentagon.", "Minister Polōnus dīcit: perpetua praesentia mīlitum Americānōrum in Polōniā ā ministeriō bellī probāta est.")
pl("Perhaps American soldiers in Poland, not for a season, but for good.", "Fortasse mīlitēs Americānī in Polōniā, nōn ad tempus, sed in perpetuum.")
pl("But the last word belongs to the White House, at the beginning of December.", "Sed ultimum verbum Domūs Albae est, initiō mēnsis Decembris.")
pl("In Poland they remember the cavalry. Brave horses. We salute them.", "In Polōniā equitātum meminērunt. Equī fortēs. Eōs salūtāmus.")
pl("A medal for a soldier at home, and perhaps soldiers for good in Poland. A busy week for the Secretary of War.", "Īnsigne mīlitī domī, et fortasse mīlitēs in perpetuum in Polōniā. Hebdomas negōtiōsa ministrō bellī.")

# ---------------- world 3: Ukraine ----------------
en("Ukraine. Witkoff and Kushner flew from the Kremlin to Ireland and met Zelensky at an air base near Dublin. Zelensky: the biggest prisoner exchange of the war, a real result. Europeans will be at the next talks.")
pl("Now Ukraine.", "Nunc Ūcraīna.")
pl("Yesterday we said: Witkoff and Kushner met Putin in the Kremlin.", "Herī dīximus: Witkoff et Kushner cum Putin in Kremlinō convēnērunt.")
pl("After the Kremlin, they will meet Zelensky, in the city of Dublin.", "Post Kremlinum cum Zelensky convenient, in urbe Dublin.")
pl("And so it happened. On Thursday evening they met Zelensky at a military airfield near Dublin.", "Et ita factum est. Diē Iovis vesperī cum Zelensky convēnērunt, in campō āeriō mīlitārī prope urbem Dublin.")
pl("The talks lasted just under an hour.", "Sermōnēs paulō minus quam hōram dūrāvērunt.")
pl("Zelensky says: Russia has accepted the large exchange of prisoners.", "Zelensky dīcit: Russia magnam permūtātiōnem captīvōrum accēpit.")
pl("Zelensky says: this is a real result, very important, and successful for the families.", "Zelensky dīcit: hic est vērus ēventus, magnī mōmentī, et fēlīx familiīs.")
pl("It will be the biggest exchange of prisoners of war. Our soldiers will come home.", "Erit maxima permūtātiō captīvōrum bellī. Mīlitēs nostrī domum redībunt.")
pl("Kushner says: we cannot conclude this deal without the Europeans at the table.", "Kushner dīcit: hanc pactiōnem sine Eurōpaeīs ad mēnsam cōnficere nōn possumus.")
pl("And so the Europeans will be at the next talks, next week.", "Itaque Eurōpaeī in proximīs sermōnibus aderunt, proximā hebdomade.")
pl("A table for everyone. In the stable we have one table: the trough. Everyone is welcome. Few are polite.", "Mēnsa omnibus. In stabulō ūnam mēnsam habēmus: praesēpe. Omnēs grātī sunt. Paucī urbānī.")
pl("But Putin will not give up his demands for land, and he refuses foreign peacekeeping troops.", "Sed Putin postulāta dē terrīs nōn remittet, et mīlitēs pācis externōs recūsat.")
pl("A large exchange of prisoners, Europeans at the table, and still no peace.", "Magna permūtātiō captīvōrum, Eurōpaeī ad mēnsam, et adhūc nūlla pāx.")

# ---------------- good news ----------------
en("Something good. Tricia Johnson, a retired kindergarten teacher, found her old students' work in her attic and is sending each of them a care package: 176 so far.")
spl("Good news.", "Rēs laeta.")
pl("Tricia Johnson was a teacher of little children. Now she is retired.", "Tricia Johnson magistra parvōrum līberōrum erat. Nunc ōtiōsa est.")
pl("In her attic she found old photos and the work of her students.", "In tabulātō suō imāginēs veterēs et opera discipulōrum invēnit.")
pl("She did not throw them away. For each former student she made a gift.", "Ea nōn abiēcit. Cuique discipulō prīstinō dōnum fēcit.")
pl("In each gift: how the child wrote his name, at about five years old, his photo, and a poem by the teacher.", "In quōque dōnō: quōmodo puer nōmen suum scrīpsit, circiter quīnque annōs nātus, imāgō eius, et carmen magistrae.")
pl("Many of the students are now forty or fifty years old.", "Multī discipulī nunc quadrāgintā aut quīnquāgintā annōs nātī sunt.")
pl("She has found 176 students so far, and counting.", "Centum septuāgintā sex discipulōs adhūc invēnit, et numerat.")
pl("Johnson says: my goal is to find them all before I retire and go to heaven.", "Johnson dīcit: prōpositum meum est omnēs invenīre, antequam ōtiōsa fīam et in caelum eam.")
pl("She kept their work for forty years. In our stable we once kept a carrot for forty minutes. Then we ate it.", "Opera eōrum quadrāgintā annōs servāvit. In stabulō nostrō ōlim carōtam quadrāgintā minūtās servāvimus. Deinde eam ēdimus.")

# ---------------- opinion ----------------
en("Opinion. This is the view of The Spectator Australia, in its leading article 'Dismissal 2.0': the Albanese government is out of control and must go.")
spl("Opinion.", "Opīniō.")
pl("This is the view of The Spectator Australia, in its leading article.", "Haec est sententia Spectātōris Austrāliae, in articulō prīmō.")
pl("The Spectator says: the Albanese government is out of control.", "Spectātor dīcit: rēs pūblica Albanese sine frēnīs est.")
pl("Without a bridle. We know the feeling.", "Sine frēnīs. Hunc sēnsum nōvimus.")
pl("The Spectator says: the changes to taxes in the budget broke a promise of the Prime Minister.", "Spectātor dīcit: mūtātiōnēs tribūtōrum in ratiōne pūblicā prōmissum prīmī ministrī frēgērunt.")
pl("And The Spectator says: wholesale electricity prices may double. The interest rate has gone up seventeen times.", "Et Spectātor dīcit: pretia mercātōria ēlectricitātis duplicārī possunt. Faenus septiēs deciēs auctum est.")
pl("This government must go, but how?", "Haec rēs pūblica abīre dēbet, sed quōmodo?")
pl("The Spectator wants a convention on the Constitution, and referendums that the citizens can start.", "Spectātor conventum dē cōnstitūtiōne vult, et suffrāgia quae cīvēs ipsī incipere possunt.")
pl("Seventeen rises in the interest rate. Not one rise in the oats. We have checked the bag.", "Septiēs deciēs faenus auctum. Avēna nē semel quidem. Saccum īnspēximus.")
pl("That is the opinion of The Spectator Australia.", "Haec est opīniō Spectātōris Austrāliae.")

# ---------------- on this day ----------------
en("On this day in 565 the Emperor Justinian died in Constantinople: he rebuilt Hagia Sophia, gathered Roman law into a few books, and his general Belisarius won back Africa and Italy, and Rome.")
spl("Today in history.", "Hodiē in historiā.")
pl("Today, in the year 565, the Emperor Justinian died, at night, in the palace at Constantinople.", "Hodiē, annō quīngentēsimō sexāgēsimō quīntō, Iūstiniānus imperātor mortuus est, noctū, in palātiō Cōnstantīnopolī.")
pl("He was perhaps the last Roman emperor whose own language was Latin.", "Fortasse ultimus imperātor Rōmānus erat cuius lingua patria Latīna erat.")
pl("His wife was Theodora. She would not flee in the great riot of 532.", "Uxor eius erat Theodōra. In magnā sēditiōne annī quīngentēsimī trīcēsimī secundī fugere nōluit.")
pl("Justinian built a new Hagia Sophia, a very great church.", "Iūstiniānus novam Hagiam Sophiam aedificāvit, ecclēsiam maximam.")
pl("His scholars gathered all of Roman law into a few books.", "Doctī eius tōtum iūs Rōmānum in paucōs librōs collēgērunt.")
pl("All Roman law in a few books. The law of the stable is shorter: one line. More oats.", "Tōtum iūs Rōmānum in paucīs librīs. Lēx stabulī brevior est: ūnus versus. Plūs avēnae.")
pl("His general Belisarius won back Africa, then Italy, and Rome itself.", "Dux eius Belisārius Āfricam recēpit, deinde Ītaliam, et Rōmam ipsam.")
pl("Belisarius and his cavalry. Many horseshoes, much glory.", "Belisārius et equitātus eius. Multae soleae, multa glōria.")
pl("Marcus and Lucius, as always, were there. But that is another story.", "Mārcus et Lūcius, ut semper, aderant. Sed id alia fābula est.")

# ---------------- summary ----------------
en("The day in brief.")
spl("Summary of the news.", "Summa rērum.")
pl("In Canberra today 28 degrees, showers, and perhaps thunder.", "Canberrae hodiē duodētrīgintā gradūs, imbrēs, et fortasse tonitrus.")
pl("The Government is considering a retreat on the backpackers.", "Rēs pūblica dē receptū dē viātōribus cōgitat.")
pl("Perhaps the ballot will wait, and the third-year visas will go up to 25,000.", "Fortasse sortītiō differētur, et licentiae annī tertiī ad vīgintī quīnque mīlia augēbuntur.")
pl("Iran says: no talks about inspections, while threats remain.", "Īrānia dīcit: nūllī sermōnēs dē īnspectiōnibus, dum minae manent.")
pl("Iran says: we have destroyed an American radar. America says: no damage.", "Īrānia dīcit: speculātōrium Americānum dēlēvimus. America dīcit: nūllum damnum.")
pl("American soldiers perhaps in Poland for good. The White House decides in December.", "Mīlitēs Americānī fortasse in perpetuum in Polōniā. Domus Alba mēnse Decembrī dēcernet.")
pl("Zelensky met Witkoff and Kushner near Dublin. Our soldiers will come home, he says.", "Zelensky cum Witkoff et Kushner prope urbem Dublin convēnit. Mīlitēs nostrī domum redībunt, inquit.")
pl("The Europeans will be at the next talks.", "Eurōpaeī in proximīs sermōnibus aderunt.")
pl("A retired teacher has found 176 former students.", "Magistra ōtiōsa centum septuāgintā sex discipulōs prīstinōs invēnit.")
pl("The Spectator says: this government must go.", "Spectātor dīcit: haec rēs pūblica abīre dēbet.")
pl("Justinian died on this day, in the year 565.", "Iūstiniānus hōc diē mortuus est, annō quīngentēsimō sexāgēsimō quīntō.")

# ---------------- words of the day ----------------
en("The words of the day. Five sentences, slowly.")
spl("The words of the day.", "Verba diēī.")
pl("The Government is considering a retreat.", "Rēs pūblica dē receptū cōgitat.")
pl("Who will pick the fruit? Who will bring in the hay?", "Quis pōma carpet? Quis faenum condet?")
pl("No talks about inspections, while threats remain.", "Nūllī sermōnēs dē īnspectiōnibus, dum minae manent.")
pl("The radar is not even scratched.", "Speculātōrium nē rāsum quidem est.")
pl("Our soldiers will come home.", "Mīlitēs nostrī domum redībunt.")
pl("Again.", "Iterum.")
pl("The Government is considering a retreat.", "Rēs pūblica dē receptū cōgitat.")
pl("Who will pick the fruit? Who will bring in the hay?", "Quis pōma carpet? Quis faenum condet?")
pl("No talks about inspections, while threats remain.", "Nūllī sermōnēs dē īnspectiōnibus, dum minae manent.")
pl("The radar is not even scratched.", "Speculātōrium nē rāsum quidem est.")
pl("Our soldiers will come home.", "Mīlitēs nostrī domum redībunt.")
pl("That was the news, straight from the horse's mouth. Goodbye, listeners. Again tomorrow.", "Haec fuērunt nūntia ex ōre equī. Valēte, audītōrēs. Crās iterum.")
p1pl("Now everything again, in Latin only.", "Nunc omnia iterum, Latīnē tantum.")

job = {
 "type": "news", "date": "2026-11-14", "music": "v5",
 "title": "Ex Ōre Equī · Diēs Sāturnī, a.d. XVIII Kal. Dec. (Sat 14 Nov 2026)",
 "summary": ("Canberra: 13–28°, partly cloudy, showers very likely (90%), thunderstorm chance this afternoon; 13–27° and showers tomorrow. "
             "Australia: Bowen pushes a pragmatic deal at COP31; two months after Tony Burke announced cuts to backpacker visas (second-year cap "
             "45,000 from 57,000, third-year 5,000 from 31,000, a ballot), the Government considers a backdown after an outcry from farms and "
             "hospitality; The Australian: the ballot may be delayed and third-year visas lifted to 25,000; Burke: 'Those conversations are "
             "continuing'; Grattan (The Conversation): the government is in trouble. Iran: Iran tells the IAEA no monitoring talks under 'persistent, explicit, and "
             "public threats by the President'; Trump: 'No, without hesitation'; IRGC claims a US radar in Bahrain, CENTCOM: two drones shot down, "
             "no damage; more tankers hit in Hormuz (some by mines); Brent about $96; Bessent moves to a military base. US: Poland's defence minister says "
             "the Pentagon has green-lit a permanent US troop presence, White House decision in early December. Ukraine: Zelensky meets Witkoff "
             "and Kushner at Casement Aerodrome, Baldonnel: 'a real result', the biggest POW exchange; Kushner: no deal 'without the Europeans "
             "being at the table'; Europeans at next week's talks. Good news: retired teacher Tricia Johnson has sent care packages to 176 former "
             "students. Opīniō: The Spectator Australia leader 'Dismissal 2.0'. Justinian died 14 Nov 565. Every line in English, then Latin; "
             "then all the Latin again. Sources: Bureau of Meteorology; ABC News (13 Nov, citing The Australian); Fox News, Jerusalem Post, "
             "Democracy Now, Just Security (13 Nov); TheJournal.ie, Irish Times/PA, Kyiv Independent (12 Nov); Only Good News Daily (13 Nov); "
             "The Spectator Australia; Christian History Institute; History Today."),
 "lines": L,
}
if __name__ == "__main__":
    json.dump(job, open("jobs/0073-news-2026-11-14.json", "w"), ensure_ascii=False, indent=1)
    lat = [r[-1] for k, *r in L if k != 'en']
    w = sum(len(t.split()) for t in lat)
    import re
    bad = [t for t in lat if re.search(r'\d', t)]
    print(len(L), 'lines ·', len(lat), 'Latin lines ·', w, 'Latin words · digits:', bad)
