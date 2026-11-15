# Ex Ōre Equī · Monday 16 November 2026 (a.d. XVI Kal. Dec.). Free voices (Jenny + Paola). English → Latin on every line, then all the Latin again.
# Sources (read 16 Nov 2026, early morning, Canberra): Bureau of Meteorology place pages (Canberra Central, The Rocks, East Melbourne,
# Brisbane City, Mount Hawthorn, North Hobart, Berrimah) · AAP via Scone Advocate 13 Nov, ABC 13 Nov, Nationals Victoria 14 Nov,
# AAP via Canberra Times 16 Nov, ABC 14 and 15 Nov (backpackers, Senate, hot mic, Manila) · Fox News live 15 Nov, The New Arab 14 Nov,
# RTÉ/Reuters 13 Nov, ABC News (US) 13 Nov, Al Jazeera 14 Nov (Iran, Bahrain, Shenzhen) · US DOT 14 Nov, ABC This Week 15 Nov,
# Deseret News 14 Nov, The Hill 14 Nov (FAA ground stop, Hegseth) · Kyiv Post 14 Nov, RTÉ 13 Nov, Irish Times 14 Nov, Il Sole 24 Ore 15 Nov
# (Ukraine) · WNDU 12 Nov, Al Jazeera 14 Nov (William) · The Spectator Australia 14 Nov (Rebecca Weisser) · Wikipedia, Tiberius.
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
pl("Today is Monday, the sixteenth day before the Kalends of December.", "Hodiē est diēs Lūnae, ante diem sextum decimum Kalendās Decembrēs.")
pl("In the year 2026.", "Annō bis mīllēsimō vīcēsimō sextō.")
pl("Monday. The week begins. The hay does not care.", "Diēs Lūnae. Hebdomas incipit. Faenō nōn cūrae est.")
pl("First, the weather. Then Australian affairs.", "Prīmum tempestās. Deinde rēs Austrāliae.")
pl("Then the world: Iran, America, Ukraine.", "Deinde orbis terrārum: Īrānia, America, Ūcraīna.")
pl("Then a happy story, opinion, and today in history.", "Tum rēs laeta, opīniō, et hodiē in historiā.")
pl("At the end, the words of the day.", "In fīne, verba diēī.")

# ---------------- weather ----------------
en("The weather. Canberra: 9 to 20 degrees, cloudy, a 40% chance of showers, mostly in the morning. Tomorrow mostly sunny: 7 to 26.")
spl("The weather.", "Tempestās.")
pl("First, Canberra.", "Prīmum Canberra.")
pl("Yesterday we said: tomorrow it will be cooler. The sky will be cloudy, and perhaps rain.", "Herī dīximus: crās frīgidius erit. Caelum nūbilum erit, et fortasse pluvia.")
pl("And so it is. Today in Canberra the sky is cloudy.", "Et ita est. Hodiē Canberrae caelum nūbilum est.")
pl("In the morning 9 degrees.", "Māne novem gradūs.")
pl("In the afternoon 20 degrees.", "Post merīdiem vīgintī gradūs.")
pl("Showers are possible: 40 per cent. Mostly in the morning.", "Imbrēs possibilēs sunt: quadrāgintā per centum. Māxime māne.")
pl("Tomorrow, Tuesday, it will be warmer. The sky will be mostly clear.", "Crās, diē Mārtis, calidius erit. Caelum ferē serēnum erit.")
pl("Tomorrow morning 7 degrees, in the afternoon 26.", "Crās māne septem gradūs, post merīdiem vīgintī sex.")
pl("Rain today, sun tomorrow. Good grass, and then the flies.", "Hodiē pluvia, crās sōl. Bona herba, et deinde muscae.")
pl("Now the other cities.", "Nunc cēterae urbēs.")
pl("In Sydney showers, and heavy rain. 20 degrees.", "Sydnēiae imbrēs, et pluvia gravis. Vīgintī gradūs.")
pl("In Melbourne cloudy, perhaps an early shower. 16 degrees.", "Melburnī caelum nūbilum, fortasse imber mātūtīnus. Sēdecim gradūs.")
pl("In Brisbane thunder is likely, perhaps severe. 31 degrees.", "Brisbanae tonitrus probābilis est, fortasse gravis. Ūnus et trīgintā gradūs.")
pl("In Perth the sky mostly clear, perhaps thunder in the evening. 29 degrees.", "Perthī caelum ferē serēnum, vesperī fortasse tonitrus. Ūndētrīgintā gradūs.")
pl("In Hobart partly cloudy. 19 degrees.", "Hobartī caelum partim nūbilum. Ūndēvīgintī gradūs.")
pl("In Darwin showers, and thunder in the afternoon. 35 degrees.", "Darwīnī imbrēs, et post merīdiem tonitrus. Trīgintā quīnque gradūs.")
pl("About Adelaide we have no new report today.", "Dē Adēlāidā hodiē nūntium novum nōn habēmus.")
pl("That is the weather.", "Haec est tempestās.")

# ---------------- Australia ----------------
en("Australia. Tony Burke on the backpacker visas: 'It's an improvement on implementation', not a backdown. The ballot is delayed to next year. The Nationals: 'Labor's backpacker backflip the latest example of their incompetence.' The Senate sits from today, with the gas reserve. And the hot-mic gaffe at COP31: Jane Hume: 'The only thing you've attracted to Australia is ridicule on the world stage.'")
spl("Australian affairs.", "Rēs Austrāliae.")
pl("Yesterday we said: the retreat on the backpackers is near.", "Herī dīximus: receptus dē viātōribus prope est.")
pl("Burke said: I am completely open to that.", "Burke dīxit: omnīnō apertus sum.")
pl("But Burke says: this is not a retreat.", "Sed Burke dīcit: hic nōn est receptus.")
pl("Burke says: it is an improvement in the carrying out.", "Burke dīcit: ēmendātiō est in exsecūtiōne.")
pl("The visas for a third year: perhaps from 5,000 to 25,000.", "Licentiae annī tertiī: fortasse ā quīnque mīlibus ad vīgintī quīnque mīlia.")
pl("And the ballot for the visas is put off to next year.", "Et sortītiō licentiārum in annum proximum differtur.")
pl("Not a retreat: an improvement in the carrying out. When a horse refuses a fence, he says the same thing.", "Nōn receptus: ēmendātiō in exsecūtiōne. Cum equus saepem recūsat, idem dīcit.")
pl("The Nationals do not believe it. Anne Webster says: Labor's backflip is the latest example of their incompetence.", "Nātiōnālēs nōn crēdunt. Anne Webster dīcit: receptus Labōrānōrum novissimum exemplum est imperītiae eōrum.")
pl("Now the parliament. From today the Senate sits.", "Nunc comitia. Ab hodiernō diē senātus sedet.")
pl("The great question: a reserve of gas for Australians.", "Magna quaestiō: cōpia gas Austrāliānīs servāta.")
pl("The plan: up to 20 per cent of the gas sent abroad will stay in Australia.", "Cōnsilium: usque ad vīgintī per centum gas quod trāns mare mittitur in Austrāliā manēbit.")
pl("The Labor party needs the Coalition, or the Greens.", "Labōrānī Coalitiōnem aut Viridēs requīrunt.")
pl("And the Prime Minister? He is in Manila, and on Wednesday he will fly to China.", "Et prīmus minister? Manīlae est, et diē Mercuriī in Sīnās volābit.")
pl("Before Manila there was COP31. There Albanese and Bowen made a joke, next to a microphone. The microphone was on.", "Ante Manīlam erat conventus dē climate. Ibi Albanese et Bowen iocum fēcērunt, prope microphōnum. Microphōnum apertum erat.")
pl("Jane Hume of the Liberals says: the only thing you have attracted to Australia is ridicule on the world stage.", "Iāna Hume Līberālium dīcit: sōlum quod in Austrāliam attrāxistis est dērīsus in scaenā orbis terrārum.")
pl("Albanese said sorry. He said: no one was hurt or harmed.", "Albanese veniam petīvit. Dīxit: nēmō laesus est.")
pl("Retreat on the backpackers, the ballot put off, gas in the Senate, a joke at the microphone. A long week ahead.", "Receptus dē viātōribus, sortītiō dīlāta, gas in senātū, iocus ad microphōnum. Longa hebdomas īnstat.")
pl("That is the state of Australia today.", "Haec est rēs Austrāliae hodiē.")

# ---------------- world 1: Iran ----------------
en("The world. Iran fires six drones at an American radar in Bahrain; Bahrain says it destroyed the attacks. Iran lifts its own 2,000-km limit on missiles. Brent oil $96.67. Trump flies to Asia today; on Thursday he meets Xi and Putin in Shenzhen.")
spl("The world.", "Orbis terrārum.")
pl("First, Iran.", "Prīmum Īrānia.")
pl("Yesterday we said: Trump is considering holding back from new attacks on Iran.", "Herī dīximus: Trump cōgitat ā novīs impetibus in Īrāniam abstinēre.")
pl("Unless Iran, or the Houthis of Yemen, start new trouble.", "Nisi Īrānia, aut Hūthī Yemeniae, nova incitāmenta faciant.")
pl("Today: new trouble. The Revolutionary Guards say: we sent six drones against an American radar in Bahrain.", "Hodiē: nova incitāmenta. Custōdēs Revolūtiōnis dīcunt: sex fūcōs contrā speculātōrium Americānum in Bahrainiā mīsimus.")
pl("Bahrain says: we destroyed the attacks.", "Bahrainia dīcit: impetūs dēlēvimus.")
pl("Neither America nor Bahrain confirms any damage.", "Neque America neque Bahrainia ūllum damnum cōnfirmat.")
pl("It is the second attack in three days.", "Est secundus impetus intrā trēs diēs.")
pl("Then the Revolutionary Guards say: the old limit on our missiles is gone. The limit was 2,000 kilometres.", "Deinde Custōdēs Revolūtiōnis dīcunt: terminus vetus missilium nostrōrum sublātus est. Terminus erat duo mīlia chiliometrōrum.")
pl("Two thousand kilometres. Even the best horse wants oats after forty kilometres.", "Duo mīlia chiliometrōrum. Etiam optimus equus post quadrāgintā chiliometra avēnam vult.")
pl("The Strait of Hormuz is still shut. The price of oil: about 97 dollars a barrel.", "Fretum Hormuziānum adhūc clausum est. Pretium oleī: circiter nōnāgintā septem dollarī prō dōliō.")
pl("On Tuesday the Foreign Minister of Iran will go to Oman, for talks.", "Diē Mārtis minister rērum externārum Īrāniae in Omaniam ībit, ad sermōnēs.")
pl("And today Trump flies to Asia. On Thursday he will meet Xi and Putin, in the city of Shenzhen.", "Et hodiē Trump in Asiam volat. Diē Iovis cum Xi et Putin conveniet, in urbe Shenzhen.")
pl("An American official says: do not expect any agreement.", "Magistrātus Americānus dīcit: nōlīte ūllam pactiōnem exspectāre.")
pl("Drones in Bahrain, missiles without a limit, the Strait still shut, and on Thursday three great men at one table.", "Fūcī in Bahrainiā, missilia sine terminō, fretum adhūc clausum, et diē Iovis trēs virī magnī ad ūnam mēnsam.")

# ---------------- world 2: US ----------------
en("America. On Friday a nationwide ground stop: for more than four hours no flight took off. 3,500 aircraft in the air all landed safely. Sean Duffy: 'we don't believe this was cyber at all', 'an incredibly old telecommunication system'. Hegseth: the charges will likely die on 3 January; Democrats plan to bring them back.")
pl("Now the United States of America.", "Nunc Cīvitātēs Foederātae Americae.")
pl("Yesterday we said: a strange week for the Secretary of War: charges, silence, a medal.", "Herī dīximus: hebdomas mīra ministrō bellī: crīmina, silentium, īnsigne.")
pl("The charges against Hegseth will probably die in January, with the old Congress. But the Democrats say: we will bring back the charges.", "Crīmina contrā Hegseth mēnse Iānuāriō probābiliter morientur, cum comitiīs veteribus. Sed Dēmocratae dīcunt: crīmina reportābimus.")
pl("Today a new story. On Friday, in all America, the aeroplanes were held on the ground.", "Hodiē nova fābula. Diē Veneris, in tōtā Americā, aëroplana in terrā retenta sunt.")
pl("For more than four hours, no aeroplane took off.", "Plūs quam quattuor hōrās nūllum aëroplanum ascendit.")
pl("It is only the second time since the attacks of September 2001.", "Hoc tantum iterum factum est post impetūs mēnsis Septembris annī bis mīllēsimī prīmī.")
pl("3,500 aeroplanes were in the air. All landed safely.", "Tria mīlia quīngenta aëroplana in caelō erant. Omnia tūtō dēscendērunt.")
pl("The Secretary of Transport, Sean Duffy, says: we don't believe this was cyber at all.", "Minister vehiculōrum, Sean Duffy, dīcit: nōn crēdimus hoc omnīnō cyberneticum fuisse.")
pl("And Duffy says: we have an incredibly old telecommunication system.", "Et Duffy dīcit: systēma nūntiōrum incrēdibiliter vetus habēmus.")
pl("An incredibly old system. Older than the horseshoe? No. But it is catching up.", "Systēma incrēdibiliter vetus. Vetustius quam solea? Nōn. Sed appropinquat.")

# ---------------- world 3: Ukraine ----------------
en("Ukraine. The exchange of 1,200 to 1,300 prisoners each is still awaited. The next talks: Abu Dhabi, this week, with the Europeans. Peskov: without agreement with Europe, Russia will use force. Saturday night: 132 Russian drones, 106 shot down. Zelensky: 'This war must be ended first.'")
pl("Now Ukraine.", "Nunc Ūcraīna.")
pl("Yesterday we said: Zelensky says: 1,200 or 1,300 prisoners, from each side.", "Herī dīximus: Zelensky dīcit: mīlle ducentī aut mīlle trecentī captīvī, ab utrāque parte.")
pl("It will be the biggest exchange of prisoners of the whole war.", "Erit maxima permūtātiō captīvōrum tōtīus bellī.")
pl("Today: the exchange has not yet happened. The final number is still being discussed.", "Hodiē: permūtātiō nōndum facta est. Numerus fīnālis adhūc tractātur.")
pl("The next talks: in the city of Abu Dhabi, this week. And the Europeans will sit at the table.", "Proximī sermōnēs: in urbe Abu Dhabi, hāc hebdomade. Et Eurōpaeī ad mēnsam sedēbunt.")
pl("But Peskov, in the Kremlin, says: if there is no agreement with Europe, Russia will use force.", "Sed Peskov, in Kremlinō, dīcit: sī nūlla pactiō cum Eurōpā erit, Russia vī ūtētur.")
pl("Zelensky says: this war must be ended first.", "Zelensky dīcit: hoc bellum prīmum fīniendum est.")
pl("And on Saturday night Russia sent 132 drones. Ukraine brought down 106.", "Et nocte Sāturnī Russia centum trīgintā duōs fūcōs mīsit. Ūcraīna centum sex dēiēcit.")
pl("In one week, more than 2,300 drones, says Zelensky.", "Ūnā hebdomade plūs quam duo mīlia trecentī fūcī, dīcit Zelensky.")
pl("Once wars had cavalry. Now drones. Drones eat no oats. That is their only virtue.", "Ōlim bella equitātum habēbant. Nunc fūcōs. Fūcī avēnam nōn edunt. Haec sōla virtūs eōrum est.")
pl("The exchange awaited, Europeans at the table, the Kremlin threatens force, and still no peace.", "Permūtātiō exspectāta, Eurōpaeī ad mēnsam, Kremlinum vim minātur, et adhūc nūlla pāx.")

# ---------------- good news ----------------
en("Something good, the next chapter. Yesterday: William, 17, found after six days near Walhalla. Today the details: the helicopter crew first saw his tackle box in the bush, then William by a creek. Police: 'Amazingly, William is in good spirits and, for the most part, in good health.' His mother cried as she hugged him.")
spl("Good news.", "Rēs laeta.")
pl("Yesterday we said: a helicopter found William, after six days in the bush.", "Herī dīximus: helicoptērum Gulielmum invēnit, post sex diēs in silvā.")
pl("Today we know how.", "Hodiē scīmus quōmodo.")
pl("From the helicopter the men first saw a small box, a fisherman's box, in the bushes.", "Ex helicoptērō virī prīmum capsulam vīdērunt, capsulam piscātōris, in dūmīs.")
pl("Then, near the box, by a stream: William.", "Deinde, prope capsulam, ad rīvum: Gulielmus.")
pl("A fisherman's box saved a life. Put it on the coat of arms of Victoria.", "Capsula piscātōris vītam servāvit. Pōnite eam in īnsignibus Victōriae.")
pl("The police say: amazingly, William is in good spirits, and mostly in good health.", "Vigilēs dīcunt: mīrābile dictū, Gulielmus bonō animō est, et ferē bene valet.")
pl("He had sunburn, and small injuries.", "Ā sōle adustus erat, et parva vulnera habēbat.")
pl("His mother cried, and held him tight.", "Māter eius flēbat, et eum artē amplexa est.")
pl("And she says: he will stay home forever.", "Et dīcit: domī manēbit in perpetuum.")
pl("Six days in the bush, and home forever. In the stable, that is called a good trade. There is hay.", "Sex diēs in silvā, et domī in perpetuum. In stabulō hoc bonum commercium vocātur. Faenum est.")

# ---------------- opinion ----------------
en("Opinion. This is the view of Rebecca Weisser, in The Spectator Australia: 'Turkish delight'. Bowen signed a $32,000 coffee contract for the COP pavilion; $147.8 million for COP activities; power prices could almost double by 2029. 'Perhaps the only way to bring down Australian electricity prices is by keeping Albanese and Bowen out of the country.'")
spl("Opinion.", "Opīniō.")
pl("This is the view of Rebecca Weisser, in The Spectator Australia.", "Haec est sententia Rebeccae Weisser, in Spectātōre Austrāliae.")
pl("Yesterday we said: De Percy says: in his speech Albanese did not say the word coal.", "Herī dīximus: De Percy dīcit: in ōrātiōne suā Albanese verbum carbō nōn dīxit.")
pl("Weisser says: Bowen came to the conference with a contract for coffee. 32,000 dollars.", "Weisser dīcit: Bowen ad conventum vēnit cum pactiōne dē coffeā. Trīgintā duo mīlia dollarōrum.")
pl("Thirty-two thousand dollars of coffee. At that price, a whole cavalry eats oats for a year.", "Trīgintā duo mīlia dollarōrum coffeae. Hōc pretiō tōtus equitātus annum avēnam edit.")
pl("But Weisser says: the coffee is small. For the conference: 147 million dollars and more.", "Sed Weisser dīcit: coffea rēs parva est. Prō conventū: centum quadrāgintā septem mīliōnēs dollarōrum et amplius.")
pl("Weisser says: the price of electricity will almost double, up to the year 2029.", "Weisser dīcit: pretium ēlectricitātis paene duplicābitur, usque ad annum bis mīllēsimum vīcēsimum nōnum.")
pl("And Weisser says: Europe found the quickest way to reduce carbon: stop counting it. The carbon dioxide had not disappeared. It only had a new address.", "Et Weisser dīcit: Eurōpa viam celerrimam invēnit ad carbōnem minuendum: eum nōn numerāre. Dioxidum carbōnis nōn ēvānuerat. Tantum novam īnscrīptiōnem habēbat.")
pl("Weisser writes: perhaps the only way to bring down the price of electricity is to keep Albanese and Bowen out of the country.", "Weisser scrībit: fortasse sōla via ad pretium ēlectricitātis minuendum est Albanese et Bowen extrā patriam tenēre.")
pl("That is the opinion of Rebecca Weisser.", "Haec est opīniō Rebeccae Weisser.")

# ---------------- on this day ----------------
en("On this day in 42 BC Tiberius was born in Rome, son of Livia. Augustus married his mother and later adopted him. Emperor from AD 14 to 37; from AD 26 on Capri. He died aged 77; Caligula followed him, the man who, the story says, wanted to make his horse Incitatus consul.")
spl("Today in history.", "Hodiē in historiā.")
pl("Today, in the year 42 before Christ, Tiberius was born, in Rome.", "Hodiē, annō quadrāgēsimō secundō ante Chrīstum, Tiberius nātus est, Rōmae.")
pl("His mother was Livia. Later Livia married Octavian: the future Augustus.", "Māter eius erat Līvia. Posteā Līvia Octāviānō nūpsit: Augustō futūrō.")
pl("Augustus adopted him as son and heir. In the year 14 Tiberius became emperor.", "Augustus eum fīlium et hērēdem adoptāvit. Annō quārtō decimō Tiberius imperātor factus est.")
pl("In the year 26 he went away to the island of Capri. Sejanus ran things in Rome.", "Annō vīcēsimō sextō in īnsulam Capreās sē recēpit. Sēiānus Rōmae rēs gerēbat.")
pl("A retreat to Capri. Burke would call it an improvement in the carrying out.", "Receptus in Capreās. Burke id ēmendātiōnem in exsecūtiōne vocāret.")
pl("He died in the year 37, aged 77. After him came Caligula.", "Mortuus est annō trīcēsimō septimō, septuāgintā septem annōs nātus. Post eum vēnit Caligula.")
pl("And Caligula, the story says, wished to make his horse Incitatus consul. Tiberius never did that. A great mistake.", "Et Caligula, ut fertur, equum suum Incitātum cōnsulem facere voluit. Tiberius hoc numquam fēcit. Magnus error.")
pl("Marcus and Lucius, as always, were there. But that is another story.", "Mārcus et Lūcius, ut semper, aderant. Sed id alia fābula est.")

# ---------------- summary ----------------
en("The day in brief.")
spl("Summary of the news.", "Summa rērum.")
pl("In Canberra today 20 degrees and showers. Tomorrow 26 and sun.", "Canberrae hodiē vīgintī gradūs et imbrēs. Crās vīgintī sex et sōl.")
pl("Burke says: not a retreat, but an improvement in the carrying out.", "Burke dīcit: nōn receptus, sed ēmendātiō in exsecūtiōne.")
pl("The ballot for the visas is put off to next year.", "Sortītiō licentiārum in annum proximum differtur.")
pl("The Senate sits from today. The great question: gas for Australians.", "Senātus ab hodiernō diē sedet. Magna quaestiō: gas Austrāliānīs.")
pl("Iran sent six drones against an American radar in Bahrain.", "Īrānia sex fūcōs contrā speculātōrium Americānum in Bahrainiā mīsit.")
pl("The old limit on Iran's missiles is gone.", "Terminus vetus missilium Īrāniae sublātus est.")
pl("On Thursday Trump will meet Xi and Putin in China.", "Diē Iovis Trump cum Xi et Putin in Sīnīs conveniet.")
pl("In America the aeroplanes were held on the ground for more than four hours.", "In Americā aëroplana plūs quam quattuor hōrās in terrā retenta sunt.")
pl("Duffy says: we have an incredibly old telecommunication system.", "Duffy dīcit: systēma nūntiōrum incrēdibiliter vetus habēmus.")
pl("The exchange of prisoners has not yet happened.", "Permūtātiō captīvōrum nōndum facta est.")
pl("A fisherman's box saved William.", "Capsula piscātōris Gulielmum servāvit.")
pl("Weisser says: the price of electricity will almost double.", "Weisser dīcit: pretium ēlectricitātis paene duplicābitur.")
pl("Tiberius was born on this day, in the year 42 before Christ.", "Tiberius hōc diē nātus est, annō quadrāgēsimō secundō ante Chrīstum.")

# ---------------- words of the day ----------------
en("The words of the day. Five sentences, slowly.")
spl("The words of the day.", "Verba diēī.")
pl("It is an improvement in the carrying out.", "Ēmendātiō est in exsecūtiōne.")
pl("The old limit on the missiles is gone.", "Terminus vetus missilium sublātus est.")
pl("The aeroplanes were held on the ground.", "Aëroplana in terrā retenta sunt.")
pl("A fisherman's box saved a life.", "Capsula piscātōris vītam servāvit.")
pl("The price of electricity will almost double.", "Pretium ēlectricitātis paene duplicābitur.")
pl("Again.", "Iterum.")
pl("It is an improvement in the carrying out.", "Ēmendātiō est in exsecūtiōne.")
pl("The old limit on the missiles is gone.", "Terminus vetus missilium sublātus est.")
pl("The aeroplanes were held on the ground.", "Aëroplana in terrā retenta sunt.")
pl("A fisherman's box saved a life.", "Capsula piscātōris vītam servāvit.")
pl("The price of electricity will almost double.", "Pretium ēlectricitātis paene duplicābitur.")
pl("That was the news, straight from the horse's mouth. Goodbye, listeners. Again tomorrow.", "Haec fuērunt nūntia ex ōre equī. Valēte, audītōrēs. Crās iterum.")
p1pl("Now everything again, in Latin only.", "Nunc omnia iterum, Latīnē tantum.")

job = {
 "type": "news", "date": "2026-11-16", "music": "v5",
 "title": "Ex Ōre Equī · Diēs Lūnae, a.d. XVI Kal. Dec. (Mon 16 Nov 2026)",
 "summary": ("Canberra: 9–20°, cloudy, 40% chance of showers (mostly morning), light winds becoming SE 15–20 km/h; Tuesday 7–26°, mostly sunny. "
             "Sydney 20 (showers, heavy rain), Melbourne 16, Brisbane 31 (storms), Perth 29, Hobart 19, Darwin 35. "
             "Australia: Burke on backpacker visas: 'It's an improvement on implementation', not a backdown; third-year cap may rise from 5,000 to 25,000; "
             "ballot delayed to next year; Nationals (Anne Webster): 'Labor's backpacker backflip the latest example of their incompetence'; "
             "Senate sits from 16 Nov: domestic gas reserve (up to 20% of exports), Labor needs Coalition or Greens; Albanese in Manila, to Shenzhen Wednesday; "
             "COP31 hot-mic gaffe: Jane Hume 'The only thing you've attracted to Australia is ridicule on the world stage'; Albanese apologised; "
             "ABC (Jacob Greber): 'The government is floundering'. "
             "Iran: IRGC says 6 drones fired at a US radar at Bahrain's Al-Rifaa base; Bahrain says attacks destroyed, no damage confirmed; second attack in 3 days; "
             "IRGC lifts its self-imposed 2,000-km missile-range limit; Hormuz still shut; Brent $96.67 (Fri); Araghchi to Muscat Tuesday; Trump leaves for Manila "
             "Monday, Xi–Putin trilateral in Shenzhen Thursday; US official: 'do not expect to get any kind of agreement'. "
             "US: Friday's nationwide FAA ground stop (4+ hours, second since 9/11), 3,500 aircraft landed safely; Duffy: 'we don't believe this was cyber at all', "
             "'an incredibly old telecommunication system'; Hegseth articles likely die 3 Jan, Democrats plan to bring them back. "
             "Ukraine: POW swap (1,200–1,300 each) still pending; next talks in Abu Dhabi this week with Europeans; Peskov: force if no deal with Europe; "
             "Zelensky: 'This war must be ended first'; 132 drones on 14–15 Nov, 106 downed; 2,300+ in a week. Good news: how William was found (tackle box seen "
             "from the helicopter); police: 'Amazingly, William is in good spirits'. Opīniō: Rebecca Weisser, 'Turkish delight' (Spectator Australia): $32,000 coffee "
             "contract, $147.8m for COP, power prices almost double by 2029. Tiberius born 16 Nov 42 BC. Every line in English, then Latin; then all the Latin again. "
             "Sources: Bureau of Meteorology; AAP; ABC; Nationals Victoria; Fox News; The New Arab; RTÉ/Reuters; ABC News; Al Jazeera; US DOT; Deseret News; "
             "The Hill; Kyiv Post; Irish Times; Il Sole 24 Ore; WNDU; The Spectator Australia; Wikipedia."),
 "lines": L,
}
if __name__ == "__main__":
    json.dump(job, open("jobs/0080-news-2026-11-16.json", "w"), ensure_ascii=False, indent=1)
    lat = [r[-1] for k, *r in L if k != 'en']
    w = sum(len(t.split()) for t in lat)
    import re
    bad = [t for t in lat if re.search(r'\d', t)]
    print(len(L), 'lines ·', len(lat), 'Latin lines ·', w, 'Latin words · digits:', bad)
