# Ex Ōre Equī · Thursday 26 November 2026 (a.d. VI Kal. Dec.). Free voices (Jenny + Paola). English → Latin on every line, then all the Latin again.
# Sources (read 26 Nov 2026, early morning, Canberra): Bureau of Meteorology place pages (Canberra Central, MS25, East Melbourne, Brisbane City,
# Novar Gardens, Marrara) + WillyWeather (The Rocks, Como, Sandy Bay) · CommBank, investingLive, PS News/AAP, The Nightly 25 Nov (CPI) ·
# ABC, The Nightly, Yahoo 25 Nov (Solomon Islands treaty) · ABC live blog via NewsLantern 25 Nov (gas bill, trust tax) · The National, FinScans,
# TVG Daily Brief 25 Nov, New York Post (Iran) · AP via Local10, Yahoo Finance, Fox Business, Forbes, Boston Report 25 Nov (US) ·
# Ukrinform, Kyiv Post, Euronews 25 Nov, Censor.net 24 Nov, Interfax-Ukraine, Ukrayinska Pravda via Yahoo 25 Nov (Ukraine) ·
# The Washington Post 25 Nov (owl) · The Spectator Australia 25 Nov (Rebecca Weisser) · New Advent, Vatican City State (St Leonard of Port Maurice).
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
pl("Today is Thursday, the sixth day before the Kalends of December.", "Hodiē est diēs Iovis, ante diem sextum Kalendās Decembrēs.")
pl("In the year 2026.", "Annō bis mīllēsimō vīcēsimō sextō.")
pl("First, the weather. Then Australian affairs.", "Prīmum tempestās. Deinde rēs Austrāliae.")
pl("Then the world: Iran, America, Ukraine.", "Deinde orbis terrārum: Īrānia, America, Ūcraīna.")
pl("Then a happy story, opinion, and today in history.", "Tum rēs laeta, opīniō, et hodiē in historiā.")
pl("At the end, the words of the day.", "In fīne, verba diēī.")

# ---------------- weather ----------------
en("The weather. Canberra: 11 to 28 degrees, partly cloudy, a slight chance of a shower in the afternoon and a possible thunderstorm, 20%. Light winds, easterly in the evening. UV 11, extreme. Tomorrow 14 to 30, partly cloudy, showers likely in the afternoon, 60%.")
spl("The weather.", "Tempestās.")
pl("First, Canberra.", "Prīmum Canberra.")
pl("Yesterday we said: tomorrow it will be warmer. And it is true.", "Herī dīximus: crās calidius erit. Et vērum est.")
pl("Today in Canberra the sky is partly cloudy.", "Hodiē Canberrae caelum partim nūbilum est.")
pl("In the morning 11 degrees.", "Māne ūndecim gradūs.")
pl("In the afternoon 28 degrees.", "Post merīdiem duodētrīgintā gradūs.")
pl("In the afternoon perhaps a shower, and perhaps thunder. Rain: 20 per cent.", "Post merīdiem fortasse imber, et fortasse tonitrus. Pluvia: vīgintī per centum.")
pl("Tomorrow morning 14 degrees, in the afternoon 30. Rain: 60 per cent.", "Crās māne quattuordecim gradūs, post merīdiem trīgintā. Pluvia: sexāgintā per centum.")
pl("Rain tomorrow, so the grass will grow. Slowly. We shall wait.", "Crās pluvia, itaque herba crēscet. Lentē crēscet. Exspectābimus.")
pl("Now the other cities.", "Nunc cēterae urbēs.")
pl("In Sydney partly cloudy. 26 degrees.", "Sydnēiae caelum partim nūbilum. Vīgintī sex gradūs.")
pl("In Melbourne mostly sun; in the afternoon perhaps a shower. 29 degrees.", "Melburnī plērumque sōl; post merīdiem fortasse imber. Ūndētrīgintā gradūs.")
pl("In Brisbane showers. 29 degrees.", "Brisbanae imbrēs. Ūndētrīgintā gradūs.")
pl("In Perth sun. 25 degrees.", "Perthī sōl. Vīgintī quīnque gradūs.")
pl("In Adelaide partly cloudy. 31 degrees.", "Adēlāidae caelum partim nūbilum. Trīgintā ūnus gradūs.")
pl("In Hobart partly cloudy. 23 degrees.", "Hobartī caelum partim nūbilum. Vīgintī trēs gradūs.")
pl("In Darwin a shower or two, and perhaps thunder. 35 degrees.", "Darwīnī ūnus aut alter imber, et fortasse tonitrus. Trīgintā quīnque gradūs.")
pl("That is the weather.", "Haec est tempestās.")

# ---------------- Australia ----------------
en("Australia. October inflation came in at 4.9%, up from 4.3% in September, the highest since 2023 and above forecasts. Electricity is up 25.2% in a year as rebates ran out. Treasurer Chalmers: 'unwelcome but unsurprising'; 'We had an inflation challenge in our economy before the conflict in the Middle East.' Shadow treasurer Tim Wilson: 'inflation has defeated the Treasurer in the economy Labor built', and he warned of the risk of another rate rise. The cash rate is 4.85%; the Reserve Bank meets on 7 and 8 December. The Solomon Islands treaty was signed in Canberra. Albanese: 'With this treaty, Australia becomes the Solomon Islands' primary security partner.' Wale: the treaty 'resets our relationship with Australia' and 'elevates it to an enduring one'; on the China pact: 'I am unable to talk about that.' Lowy's Nobetau expects 'some sort of economic coercion'. The gas reserve bill had still not passed on Wednesday afternoon; Labor needs a Coalition deal; minister Tim Ayres expected a vote by Thursday, before Parliament breaks for summer. Labor and the Greens did pass the trust tax; Taylor: a 'dirty deal'.")
spl("Australian affairs.", "Rēs Austrāliae.")
pl("First, the new prices.", "Prīmum, pretia nova.")
pl("Yesterday we said: economists say: inflation will be 4.8 per cent.", "Herī dīximus: oeconomī dīcunt: īnflātiō erit quattuor per centum et octōgintā centēsimae.")
pl("Now we know. Inflation is 4.9 per cent. In September it was 4.3 per cent.", "Nunc scīmus. Īnflātiō est quattuor per centum et nōnāgintā centēsimae. Mēnse Septembrī erat quattuor per centum et trīgintā centēsimae.")
pl("Higher than the economists said. The highest since 2023.", "Altior quam oeconomī dīxērunt. Summa ab annō bis mīllēsimum vīcēsimō tertiō.")
pl("Electricity is dearer by more than 25 per cent in one year.", "Ēlectricitās ūnō annō plūs quam vīgintī quīnque per centum cārior est.")
pl("Jim Chalmers, the Treasurer, says: unwelcome, but not surprising.", "Iacōbus Chalmers, minister aerāriī, dīcit: ingrātum, sed nōn mīrum.")
pl("Unwelcome, but not surprising. In the stable we say this about the vet.", "Ingrātum, sed nōn mīrum. In stabulō hoc dē veterīnāriō dīcimus.")
pl("Tim Wilson, for the Opposition, says: inflation has defeated the Treasurer, in the economy that Labor built.", "Tim Wilson, prō oppositiōne, dīcit: īnflātiō ministrum aerāriī vīcit, in oeconomiā quam Labōrānī aedificāvērunt.")
pl("The interest rate is now 4.85 per cent. The central bank meets in December.", "Faenus nunc est quattuor per centum et octōgintā quīnque centēsimae. Argentāria centrālis mēnse Decembrī conveniet.")
pl("Now, the Pacific Ocean. Yesterday we said: a new treaty with the Solomon Islands will be signed in Canberra.", "Nunc, Ōceanus Pācificus. Herī dīximus: novum foedus cum Īnsulīs Salomōnis Canberrae signābitur.")
pl("And the treaty was signed.", "Et foedus signātum est.")
pl("Albanese says: with this treaty Australia becomes the first security partner of the Solomon Islands.", "Albanese dīcit: hōc foedere Austrālia prīma socia Īnsulārum Salomōnis dē sēcūritāte fit.")
pl("Matthew Wale says: the treaty renews our friendship with Australia, and makes it lasting.", "Matthew Wale dīcit: foedus amīcitiam nostram cum Austrāliā renovat, et perpetuam facit.")
pl("And the treaty with China? Wale says: I cannot talk about that.", "Et foedus cum Sīnīs? Wale dīcit: dē eā rē loquī nōn possum.")
pl("Now, the gas. Yesterday we said: the law about the gas has still not been passed. Two days are left.", "Nunc, gas. Herī dīximus: lēx dē gas adhūc nōn lāta est. Duo diēs restant.")
pl("Yesterday afternoon the law about the gas had still not been passed. Today is perhaps the last day of parliament this year.", "Herī post merīdiem lēx dē gas adhūc nōn lāta erat. Hodiē fortasse ultimus diēs comitiōrum huius annī.")
pl("The Labor party is looking for a deal with the Coalition.", "Labōrānī pactiōnem cum Coalitiōne quaerunt.")
pl("Yesterday we said: nobody has yet left the starting gate. Today the race may end.", "Herī dīximus: nēmō adhūc ē carceribus exiit. Hodiē curriculum fortasse fīnītur.")
pl("The horses are still in the starting gates. The crowd is going home. Someone has lost the key.", "Equī adhūc in carceribus stant. Turba domum it. Aliquis clāvem āmīsit.")

# ---------------- Iran ----------------
en("Iran. The Revolutionary Guards claim two more tankers 'exploded' and caught fire after hitting naval mines early on Wednesday, because they took a 'false route'. Not verified; no word from the US command. Trump told the New York Post the war is funded until the end of January: 'We can put that war to bed anytime we want.' 'I just don't want them to have a nuclear weapon.' Ships that challenge the blockade will end up 'at the bottom of the sea'. Iranian state media walked back reports of a convoy to break the blockade; TankerTrackers said the ship did not exist. Tasnim: Iran will 'certainly break it'. Inflation in Iran: 88.7% in October. Brent about $91.")
spl("The world. First, Iran.", "Orbis terrārum. Prīmum Īrānia.")
pl("Yesterday we said: the Revolutionary Guards say: three oil ships struck naval mines. Nobody has confirmed it.", "Herī dīximus: Custōdēs Revolūtiōnis dīcunt: trēs nāvēs oleāriae in bombās marīnās incurrērunt. Nēmō id cōnfirmāvit.")
pl("Today the Guards say: two more ships struck naval mines, exploded, and caught fire.", "Hodiē Custōdēs dīcunt: duae aliae nāvēs in bombās marīnās incurrērunt, displōsae sunt, et exārsērunt.")
pl("Again nobody has confirmed it. The Americans have said nothing.", "Iterum nēmō id cōnfirmāvit. Americānī nihil dīxērunt.")
pl("Trump tells the New York Post: the war has money until the end of January.", "Trump āctīs New York Post dīcit: bellum pecūniam habet usque ad fīnem Iānuāriī.")
pl("And he says: we can put that war to bed whenever we want.", "Et dīcit: id bellum in lectum pōnere possumus, quandōcumque volumus.")
pl("To bed. In the stable we say: to the straw. But this war, we think, will not sleep.", "In lectum. In stabulō dīcimus: in strāmentum. Sed hoc bellum, putāmus, nōn dormiet.")
pl("And: ships that challenge the blockade will end up at the bottom of the sea.", "Et: nāvēs quae obsidiōnem temptant in fundō maris fīnem habēbunt.")
pl("In Iran there was news of a ship that would break the blockade.", "In Īrāniā nūntium erat dē nāve quae obsidiōnem frangeret.")
pl("But TankerTrackers says: that ship does not exist. And the Iranian state media took the news back.", "Sed TankerTrackers dīcit: ea nāvis nōn exstat. Et nūntiī pūblicī Īrāniae nūntium revocāvērunt.")
pl("A ship that does not exist. An excellent ship. It never sinks, it is never captured, it never arrives.", "Nāvis quae nōn exstat. Optima nāvis. Numquam mergitur, numquam capitur, numquam advenit.")
pl("Tasnim says: Iran will certainly break the blockade.", "Tasnim dīcit: Īrānia obsidiōnem certē franget.")
pl("The price of oil: about 91 dollars a barrel.", "Pretium oleī: circiter nōnāgintā ūnus dollarī prō dōliō.")

# ---------------- America ----------------
en("America. A correction: on Tuesday Nvidia fell 5.9%, not about 8%. On Wednesday it fell about 8%. AP: 'Anxiety over the AI boom, inflation and tariffs drag Wall Street lower and the S&P 500 slumps 2.2%.' Trump on a pardon for Huang: 'always an option', but he did not think it would be needed. Trade Representative Jamieson Greer proposes tariffs on 14 economies, up to 20% on China, to 'level the playing field for American workers'. Today is Thanksgiving; Trump's proclamation calls it a 'tradition older than the Nation itself'. The pardoned turkeys, Freedom and Feathers, retire to Texas A&M University.")
spl("America.", "America.")
pl("Yesterday we said: Nvidia lost about 8 per cent. A correction: on Tuesday it lost almost 6 per cent.", "Herī dīximus: Nvidia circiter octō per centum āmīsit. Corrigimus: diē Mārtis paene sex per centum āmīsit.")
pl("A correction. In the stable we take corrections seriously. Usually with a carrot.", "Corrēctiō. In stabulō corrēctiōnēs graviter accipimus. Plērumque cum carōtā.")
pl("But yesterday Nvidia really did lose about 8 per cent.", "Sed herī Nvidia vērē circiter octō per centum āmīsit.")
pl("The whole market fell. AP says: anxiety about artificial intelligence, about inflation, about tariffs.", "Tōta bursa cecidit. AP dīcit: cūra dē intellegentiā artificiālī, dē īnflātiōne, dē portōriīs.")
pl("The index of the five hundred companies fell 2.2 per cent.", "Index quīngentārum societātum duo per centum et vīgintī centēsimās āmīsit.")
pl("And the tariffs. Jamieson Greer, America's trade representative, proposes new tariffs on fourteen countries.", "Et portōria. Jamieson Greer, lēgātus commerciī Americae, nova portōria in quattuordecim terrās prōpōnit.")
pl("On China up to 20 per cent. Greer says: to level the playing field for American workers.", "In Sīnās usque ad vīgintī per centum. Greer dīcit: ut campus aequus sit operāriīs Americānīs.")
pl("And today in America is Thanksgiving Day. Trump says: this custom is older than the nation itself.", "Et hodiē in Americā est diēs grātiārum āctiōnis. Trump dīcit: haec cōnsuētūdō antīquior est quam ipsa nātiō.")
pl("Yesterday we said: two turkeys were pardoned. Now they are going to a university in Texas.", "Herī dīximus: duo gallopāvōnēs veniam accēpērunt. Nunc in ūniversitātem Texiānam eunt.")

# ---------------- Ukraine ----------------
en("Ukraine. Zelensky: 'we are now waiting for the American side to provide a date for a new meeting—one that should involve four parties.' Budanov, the head of Zelensky's office: perhaps 'before Christmas'; no place yet. The prisoner exchange: late November or early December, more than 1,000 people, 'several hundred people at a time'. On Tuesday night Russia launched 112 drones; 88 were downed. On Wednesday 7 people were killed across Ukraine. A correction: the 79-year-old woman pulled from the ruins in Dymer died in hospital; the toll is 12. Ukraine hit three Russian refineries; Zelensky calls them 'long-range sanctions'; Putin: 'retaliatory measures on our part are inevitable.'")
spl("Ukraine.", "Ūcraīna.")
pl("Yesterday we said: Peskov says: the date has not yet been set.", "Herī dīximus: Peskov dīcit: diēs nōndum cōnstitūtus est.")
pl("Today Zelensky says: we are waiting for a date from the Americans, for a meeting of four sides.", "Hodiē Zelensky dīcit: diem ab Americānīs exspectāmus, ad conventum quattuor partium.")
pl("Budanov, the head of Zelensky's office, says: perhaps before Christmas.", "Budanov, prīnceps officiī Zelensky, dīcit: fortasse ante Nātālem Chrīstī.")
pl("Before Christmas. Which Christmas? Nobody said. In the stable we always ask.", "Ante Nātālem Chrīstī. Quem Nātālem? Nēmō dīxit. In stabulō hoc semper rogāmus.")
pl("And the exchange of prisoners? Budanov says: late November or early December. More than a thousand people.", "Et permūtātiō captīvōrum? Budanov dīcit: exeunte mēnse Novembrī aut ineunte Decembrī. Plūs quam mīlle hominēs.")
pl("Hardly in one day: in parts, several hundred people at a time.", "Vix ūnō diē: per partēs, aliquot centum hominēs simul.")
pl("On Tuesday night Russia sent 112 drones. Ukraine brought down 88.", "Nocte diēī Mārtis Russia centum duodecim fūcōs mīsit. Ūcraīna duodēnōnāgintā dēiēcit.")
pl("On Wednesday seven people were killed across Ukraine.", "Diē Mercuriī septem hominēs per tōtam Ūcraīnam necātī sunt.")
pl("Yesterday we said: in Dymer the dead are eleven. But the woman of 79 died in hospital. The dead are twelve.", "Herī dīximus: in oppidō Dymer mortuī sunt ūndecim. Sed fēmina ūndēoctōgintā annōrum in valētūdināriō mortua est. Mortuī sunt duodecim.")
pl("Ukraine struck three Russian oil refineries. Zelensky calls these strikes long-range sanctions.", "Ūcraīna trēs officīnās oleī Russicās percussit. Zelensky hōs ictūs poenās longinquās vocat.")
pl("Putin says: retaliation from our side is inevitable.", "Putin dīcit: ultiō nostra vītārī nōn potest.")

# ---------------- happy story ----------------
en("A happy story. On 16 November, on a North Carolina highway, Heather Henry's SUV hit a barred owl, which got stuck in the grille, alive. 'I was absolutely shocked to see that it was still alive.' She knocked on the door of a fire station in Concord; Lieutenant Caleb Miller pulled the owl out. The Carolina Wildlife Rehabilitation Center found head and leg injuries, but expects it to recover. Director Molly McMullen: 'We call this trauma season.' 'He's lucky.' Henry faces about $1,000 in repairs.")
spl("A happy story.", "Rēs laeta.")
pl("In America, in North Carolina, Heather Henry was driving her car on the highway.", "In Americā, in Carolīnā Septentriōnālī, Heather Henry autocinētum suum in viā magnā agēbat.")
pl("Her car struck an owl. The owl got stuck in the front of the car, alive.", "Autocinētum ululam percussit. Ulula in fronte autocinētī haesit, vīva.")
pl("Henry says: I was absolutely shocked when I saw it still alive.", "Henry dīcit: valdē obstupuī, cum eam adhūc vīvam vīdī.")
pl("She knocked on the door of a fire station, in the town of Concord.", "Iānuam statiōnis vigilum pulsāvit, in oppidō Concord.")
pl("A firefighter, Caleb Miller, pulled the owl out.", "Vigil Caleb Miller ululam extrāxit.")
pl("A free ride, all the way to the fire station. In the stable nobody has ever given a horse a ride.", "Vectūra grātīs, usque ad statiōnem vigilum. In stabulō nēmō umquam equum vēxit.")
pl("At the hospital for wild animals they say: the owl is hurt in the head and the leg, but it will recover.", "In valētūdināriō bēstiārum dīcunt: ulula in capite et crūre laesa est, sed convalēscet.")

# ---------------- opinion ----------------
en("Opinion. Rebecca Weisser, in The Spectator Australia: 'Jimflation soars'. 'Treasurer Jim Chalmers has spent four and a half years making sure the government lives beyond its means.' 'It is excessive government spending that fuels inflation rather than pointing his finger at fuel prices.' 'His job is to put his foot on the brake, not the accelerator.' 'Bowen came home without a deal. Chalmers still gets the bill.' And she mocks his 'unwelcome but unsurprising'.")
spl("Opinion.", "Opīniō.")
pl("This is the opinion of Rebecca Weisser, in The Spectator Australia.", "Haec est sententia Rebeccae Weisser, in Spectātōre Austrāliae.")
pl("Her title: Jim's inflation soars.", "Titulus eius: īnflātiō Iacōbī ad caelum volat.")
pl("Weisser says: for four and a half years Chalmers has made sure that the government lives beyond its means.", "Weisser dīcit: per quattuor annōs et dīmidium Chalmers cūrāvit ut rēs pūblica suprā opēs suās vīveret.")
pl("And: his job is to put his foot on the brake, not on the accelerator.", "Et: officium eius est pedem in frēnō pōnere, nōn in accelerātōre.")
pl("The brake. In the stable we know the bridle well. It is not on the foot.", "Frēnum. In stabulō frēnum bene nōvimus. In pede nōn est.")

# ---------------- history ----------------
en("Today in history. On the night of 26 November 1751 Saint Leonard of Port Maurice died in Rome. A Franciscan friar, born Paul Jerome Casanova in Porto Maurizio in 1676, he wanted to go to China as a missionary, but was told that his China would be Italy. He went barefoot. In the Holy Year 1750, at the Pope's request, he set up the Stations of the Cross in the Colosseum, which helped save it from neglect; he set up 571 other sets across Italy. Called to Rome by Benedict XIV, he arrived on the evening of 26 November and died that night at eleven.")
spl("Today in history.", "Hodiē in historiā.")
pl("On this day, in the year 1751, Saint Leonard of Port Maurice died in Rome.", "Hōc diē, annō mīllēsimō septingentēsimō quīnquāgēsimō prīmō, Sānctus Leonardus ā Portū Mauritiō Rōmae mortuus est.")
pl("He was a Franciscan friar. He wanted to go to China.", "Frāter Franciscānus erat. In Sīnās īre volēbat.")
pl("But he was told: your China will be Italy.", "Sed eī dictum est: Sīnae tuae erunt Ītalia.")
pl("And he went all through Italy, barefoot.", "Et per tōtam Ītaliam nūdīs pedibus ībat.")
pl("Barefoot! Without shoes! Our blacksmith turns pale.", "Nūdīs pedibus! Sine soleīs! Faber noster pallet.")
pl("In the Holy Year 1750, at the Pope's request, he set up the Stations of the Cross in the Colosseum.", "Annō Sānctō mīllēsimō septingentēsimō quīnquāgēsimō, Pāpā rogante, statiōnēs Viae Crucis in Colossēō posuit.")
pl("This helped to save the Colosseum from neglect.", "Hoc Colossēum ab incūriā servāre adiūvit.")
pl("He set up 571 other Ways of the Cross across Italy.", "Quīngentās septuāgintā ūnam aliās Viās Crucis per Ītaliam posuit.")
pl("On the evening of 26 November he came to Rome. That same night, at eleven o'clock, he died.", "Vesperī ante diem sextum Kalendās Decembrēs Rōmam advēnit. Eādem nocte, hōrā ūndecimā noctis, mortuus est.")

# ---------------- summary ----------------
en("The summary.")
spl("The summary.", "Summa rērum.")
pl("Inflation is 4.9 per cent. Chalmers says: unwelcome, but not surprising.", "Īnflātiō est quattuor per centum et nōnāgintā centēsimae. Chalmers dīcit: ingrātum, sed nōn mīrum.")
pl("The treaty with the Solomon Islands was signed.", "Foedus cum Īnsulīs Salomōnis signātum est.")
pl("Yesterday the law about the gas had still not been passed. Today is perhaps the last day of parliament.", "Herī lēx dē gas adhūc nōn lāta erat. Hodiē fortasse ultimus diēs comitiōrum.")
pl("Iran says: two more ships struck naval mines. Nobody has confirmed it.", "Īrānia dīcit: duae aliae nāvēs in bombās marīnās incurrērunt. Nēmō id cōnfirmāvit.")
pl("TankerTrackers says: the ship that would break the blockade does not exist.", "TankerTrackers dīcit: nāvis quae obsidiōnem frangeret nōn exstat.")
pl("The market fell. Greer proposes new tariffs on fourteen countries.", "Bursa cecidit. Greer nova portōria in quattuordecim terrās prōpōnit.")
pl("Zelensky is waiting for a date. Perhaps before Christmas.", "Zelensky diem exspectat. Fortasse ante Nātālem Chrīstī.")
pl("In North Carolina a firefighter pulled an owl out of a car.", "In Carolīnā Septentriōnālī vigil ululam ex autocinētō extrāxit.")
pl("Weisser says: Chalmers must put his foot on the brake.", "Weisser dīcit: Chalmers pedem in frēnō pōnere dēbet.")
pl("On this day in 1751 Saint Leonard died in Rome.", "Hōc diē, annō mīllēsimō septingentēsimō quīnquāgēsimō prīmō, Sānctus Leonardus Rōmae mortuus est.")

# ---------------- words of the day ----------------
en("The words of the day. Five sentences, slowly.")
spl("The words of the day.", "Verba diēī.")
W = [
 ("Unwelcome, but not surprising.", "Ingrātum, sed nōn mīrum."),
 ("A ship that does not exist never arrives.", "Nāvis quae nōn exstat numquam advenit."),
 ("New tariffs on fourteen countries.", "Nova portōria in quattuordecim terrās."),
 ("The owl got stuck in the front of the car.", "Ulula in fronte autocinētī haesit."),
 ("His job is to put his foot on the brake.", "Officium eius est pedem in frēnō pōnere."),
]
for e, t in W: pl(e, t)
pl("Again.", "Iterum.")
for e, t in W: pl(e, t)
pl("That was the news, straight from the horse's mouth. Goodbye, listeners. Again tomorrow.", "Haec fuērunt nūntia ex ōre equī. Valēte, audītōrēs. Crās iterum.")
p1pl("Now everything again, in Latin only.", "Nunc omnia iterum, Latīnē tantum.")

job = {
 "type": "news", "date": "2026-11-26", "music": "v5",
 "title": "Ex Ōre Equī · Diēs Iovis, a.d. VI Kal. Dec. (Thu 26 Nov 2026)",
 "summary": ("Canberra: 11–28°, partly cloudy, slight chance of an afternoon shower, possible thunderstorm, 20%, UV 11 (extreme). Friday 14–30°, 60%. "
             "Sydney 26, Melbourne 29 (a shower possible), Brisbane 29 (showers), Perth 25 (sunny), Adelaide 31, Hobart 23, Darwin 35 (showers, storm possible). "
             "Australia: October CPI 4.9% (Sept 4.3%), highest since 2023; electricity +25.2%; Chalmers: 'unwelcome but unsurprising'; Wilson: 'inflation has "
             "defeated the Treasurer in the economy Labor built'; cash rate 4.85%, RBA meets 7–8 Dec. Solomon Islands treaty signed in Canberra; Albanese: "
             "'primary security partner'; Wale: 'resets our relationship', on the China pact 'I am unable to talk about that'; Nobetau: 'economic coercion'. "
             "Gas reserve bill still not passed Wednesday afternoon; Ayres expected a vote by Thursday; Labor–Greens trust tax deal passed, Taylor: 'dirty deal'. "
             "Iran: IRGC claims two more tankers 'exploded' on naval mines (unverified); Trump to the NY Post: war funded to end of January, 'We can put that war "
             "to bed anytime we want', 'I just don't want them to have a nuclear weapon', blockade runners 'at the bottom of the sea'; convoy report walked back, "
             "TankerTrackers: the ship did not exist; Tasnim: Iran will 'certainly break it'; Iran inflation 88.7%; Brent ~$91. "
             "US: Nvidia −5.9% Tue (correction) and ~−8% Wed; S&P 500 −2.2% (AP); Trump: a Huang pardon 'always an option'; Greer proposes tariffs on 14 economies, "
             "up to 20% on China; Thanksgiving; turkeys Freedom and Feathers retire to Texas A&M. "
             "Ukraine: Zelensky waits for a US date for a four-party meeting; Budanov: 'before Christmas'; POW swap late Nov/early Dec, 1,000+, in stages; "
             "112 drones / 88 down; 7 killed Wednesday; Dymer toll 12 (correction); refinery strikes, 'long-range sanctions'; Putin: retaliation 'inevitable'. "
             "Good news: barred owl stuck in a car grille, pulled out at a Concord NC fire station (Washington Post). Opīniō: Rebecca Weisser, 'Jimflation soars' "
             "(Spectator Australia). St Leonard of Port Maurice d. Rome 26 Nov 1751 (Colosseum Stations of the Cross). "
             "Every line in English, then Latin; then all the Latin again. "
             "Sources: Bureau of Meteorology; WillyWeather; CommBank; investingLive; PS News/AAP; The Nightly; ABC; Yahoo; NewsLantern; The National; FinScans; "
             "TVG Daily Brief; New York Post; AP; Yahoo Finance; Fox Business; Forbes; Boston Report; Ukrinform; Kyiv Post; Euronews; Censor.net; Interfax-Ukraine; "
             "Ukrayinska Pravda; The Washington Post; The Spectator Australia; New Advent; Vatican City State."),
 "lines": L,
}
if __name__ == "__main__":
    json.dump(job, open("jobs/0093-news-2026-11-26.json", "w"), ensure_ascii=False, indent=1)
    lat = [r[-1] for k, *r in L if k != 'en']
    w = sum(len(t.split()) for t in lat)
    import re
    bad = [t for t in lat if re.search(r'\d', t)]
    print(len(L), 'lines ·', len(lat), 'Latin lines ·', w, 'Latin words · digits:', bad)
