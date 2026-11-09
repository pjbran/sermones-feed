# Ācta Diurna · Tuesday 10 November 2026. Free voices (Jenny + Paola). English → Latin on every line, then all the Latin again.
# Sources (read 10 Nov 2026, early morning, Canberra): Bureau of Meteorology, Canberra Central forecast (issued 9 Nov 8 am)
# · ABC federal politics blog 9 Nov (inflation 4.3%, over-65s rebate savings, Resolve poll) · The Age/SMH via HeadTopics 9 Nov
# (Watt on leaks against Chalmers; Taylor quote) · The National 9 Nov + Al Jazeera 9 Nov (Task Force Iron Gate, Trump Truth Social,
# Cooper, IRGC) · Just Security Early Edition 9 Nov (Trump to CNN, Rubio, Qatar PM, Ukraine substations, EU grid fund)
# · Roll Call 9 Nov (Hegseth impeachment, Jeffries) · Yahoo News midterms live 7 Nov (Mississippi, Alaska) · UN News 9 Nov
# · Reuters via Khaleej Times 2 Nov (Abu Dhabi talks, Witkoff, Kushner) · Good Good Good 7 Nov (Flint, Rx Kids)
# · The Spectator Australia: David Flint, "Political trends firming against Labor" (31 Oct) · Pope Leo I, died 10 Nov 461.
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
spl("Hello, listeners. This is the Acta Diurna.", "Salvēte, audītōrēs. Haec sunt Ācta Diurna.")
pl("Today is Tuesday, the fourth day before the Ides of November.", "Hodiē est diēs Mārtis, ante diem quārtum Īdūs Novembrēs.")
pl("In the year 2026.", "Annō bis mīllēsimō vīcēsimō sextō.")
pl("First, the weather. Then Australian affairs.", "Prīmum tempestās. Deinde rēs Austrāliae.")
pl("Then the world: Iran, America, Ukraine.", "Deinde orbis terrārum: Īrānia, America, Ūcraīna.")
pl("Then a happy story, opinion, and today in history.", "Tum rēs laeta, opīniō, et hodiē in historiā.")
pl("At the end, the words of the day.", "In fīne, verba diēī.")

# ---------------- weather ----------------
en("The weather. Canberra: fog early, then a mostly sunny, warm Tuesday. Showers possible tomorrow.")
spl("The weather.", "Tempestās.")
pl("First, Canberra.", "Prīmum Canberra.")
pl("Yesterday we said: tomorrow in the morning there may be fog.", "Herī dīximus: crās māne fortasse nebula erit.")
pl("And so it is. Today in Canberra there is fog in the morning.", "Et ita est. Hodiē Canberrae māne nebula est.")
pl("Then the sky is mostly clear.", "Deinde caelum plērumque serēnum est.")
pl("In the morning it is cold: only 4 degrees.", "Māne frīgidum est: quattuor gradūs tantum.")
pl("In the afternoon it is warm: 25 degrees.", "Post merīdiem calidum est: quīnque et vīgintī gradūs.")
pl("No rain is expected.", "Pluvia nūlla exspectātur.")
pl("At first the wind is light. At midday it blows from the north-west, 15 to 25 kilometres an hour.", "Prīmō ventus lēnis est. Merīdiē ab occidente et septentriōnibus flat, quīndecim ad vīgintī quīnque chiliometra in hōrā.")
pl("Tomorrow, Wednesday, the sky will be partly cloudy.", "Crās, diē Mercuriī, caelum partim nūbilum erit.")
pl("Tomorrow morning 9 degrees, in the afternoon 28.", "Crās māne novem gradūs, post merīdiem duodētrīgintā.")
pl("Tomorrow perhaps a shower, and in the afternoon perhaps thunder.", "Crās fortasse imber, et post merīdiem fortasse tonitrus.")
pl("Tomorrow the wind will blow from the south-east.", "Crās ventus ab austrō et oriente flābit.")
pl("So: today 25 degrees, tomorrow 28.", "Ergō: hodiē quīnque et vīgintī gradūs, crās duodētrīgintā.")
pl("In Canberra today: fog in the morning, warm in the afternoon, and no rain.", "Canberrae hodiē māne nebula, post merīdiem calidum, et sine pluviā.")
pl("Today we have no new report on the other cities.", "Dē cēterīs urbibus hodiē nūntium novum nōn habēmus.")
pl("That is the weather.", "Haec est tempestās.")

# ---------------- Australia ----------------
en("Australia. Inflation is high, Labor colleagues are leaking against the Treasurer, and only one in five Australians trusts the Prime Minister.")
spl("Australian affairs.", "Rēs Austrāliae.")
pl("Yesterday we said: Australia's economy is getting slower, and the interest rate is high.", "Herī dīximus: oeconomia Austrāliae tardior fit, et faenus altum est.")
pl("Today: inflation is high.", "Hodiē: īnflātiō alta est.")
pl("Inflation in Australia is now 4.3 per cent, as Albanese says.", "Īnflātiō in Austrāliā nunc est quattuor et trēs decimae per centum, ut Albanese dīcit.")
pl("So inflation in Australia is higher than in other countries.", "Ergō īnflātiō in Austrāliā altior est quam in aliīs terrīs.")
pl("Jim Chalmers runs the Treasury.", "Iacōbus Chalmers aerārium regit.")
pl("But now colleagues of his own party are leaking secrets against Chalmers.", "Sed nunc collēgae eiusdem factiōnis sēcrēta contrā Chalmers prōdunt.")
pl("Murray Watt, a minister, says: stop leaking secrets.", "Murray Watt, minister, dīcit: nōlīte sēcrēta prōdere.")
pl("Watt says: Chalmers is doing an excellent job, in very difficult times.", "Watt dīcit: Chalmers rem optimē gerit, temporibus valdē difficilibus.")
pl("But someone is leaking secrets. Labor is not united.", "Sed aliquis sēcrēta prōdit. Labōrānī nōn concordēs sunt.")
pl("The government wants to save 3 billion dollars.", "Rēs pūblica tria mīlliarda dollarōrum servāre vult.")
pl("It wants to cut the help that people over 65 receive for health insurance.", "Auxilium minuere vult quod hominēs plūs quam sexāgintā quīnque annōs nātī prō cūrā valētūdinis accipiunt.")
pl("But in the Senate Labor does not have a majority.", "Sed in senātū Labōrānī maiōrem partem nōn habent.")
pl("The Opposition and the Greens say no.", "Oppositiō et Viridēs negant.")
pl("And now a new poll, called Resolve.", "Et nunc nova percontātiō, quae Resolve vocātur.")
pl("Only 20 per cent of Australians trust Albanese.", "Vīgintī tantum per centum Austrāliānōrum Albanēsiō fidem habent.")
pl("One in five. Only one in five trusts Albanese.", "Ūnus ē quīnque. Ūnus tantum ē quīnque Albanēsiō fidem habet.")
pl("And more than 40 per cent blame Labor for the cost of living.", "Et plūs quam quadrāgintā per centum Labōrānōs ob pretia vītae culpant.")
pl("Angus Taylor is the leader of the Opposition.", "Angus Taylor dux oppositiōnis est.")
pl("Taylor says: the Prime Minister does not understand things, and is not equal to the task.", "Taylor dīcit: prīmus minister rēs nōn intellegit, et rēbus impār est.")
pl("And he does not control his anger, as Taylor says.", "Et īrae nōn imperat, ut Taylor dīcit.")
pl("High inflation, colleagues leaking secrets, little trust.", "Īnflātiō alta, collēgae sēcrēta prōdentēs, fidēs parva.")
pl("That is the state of Australia today.", "Haec est rēs Austrāliae hodiē.")

# ---------------- world 1: Iran ----------------
en("The world. Iran: Trump says Iron Gate is now in full force, and very little gets into, or out of, Iran.")
spl("The world.", "Orbis terrārum.")
pl("First, Iran.", "Prīmum Īrānia.")
pl("Yesterday we said: the Americans have created a new force. Its name is Iron Gate.", "Herī dīximus: Americānī novam manum creāvērunt. Nōmen eī est Porta Ferrea.")
pl("Iron Gate will watch Iran's land routes.", "Porta Ferrea viās terrestrēs Īrāniae spectābit.")
pl("Today Trump says: Iron Gate is now in full force.", "Hodiē Trump dīcit: Porta Ferrea nunc plēnā vī agit.")
pl("Trump says: almost nothing gets into Iran, or out of Iran.", "Trump dīcit: paene nihil in Īrāniam intrat, aut ex Īrāniā exit.")
pl("At sea the blockade remains.", "In marī obsidiō manet.")
pl("Because of the blockade Iran has not been able to sell oil worth more than 25 billion dollars, as the Americans say.", "Propter obsidiōnem Īrānia oleum plūs quam vīgintī quīnque mīlliardōrum dollarōrum vendere nōn potuit, ut Americānī dīcunt.")
pl("Admiral Brad Cooper says: Iron Gate strengthens our blockade at sea.", "Praefectus classis Brad Cooper dīcit: Porta Ferrea obsidiōnem nostram in marī cōnfirmat.")
pl("But a spokesman for Iran's Revolutionary Guards says: Iron Gate is only a play on words.", "Sed prōlocūtor Custōdum Revolūtiōnis Īrāniae dīcit: Porta Ferrea tantum lūdus verbōrum est.")
pl("Yesterday we said: Iran has sent a new proposal through Qatar.", "Herī dīximus: Īrānia prōpositum novum per Qatariam mīsit.")
pl("Today Rubio, the American foreign minister, says: the proposal is outrageous and ridiculous.", "Hodiē Rubio, minister rērum exterārum Americānus, dīcit: prōpositum indignum et rīdiculum est.")
pl("And the Prime Minister of Qatar met Trump and Vance, in the White House.", "Et prīmus minister Qatariae Trump et Vance convēnit, in Domō Albā.")
pl("Trump says: I will hardly order a new attack, while the talks go on.", "Trump dīcit: novum impetum vix iubēbō, dum sermōnēs prōcēdunt.")
pl("But it depends, says Trump, on whether Iran signs a very strong agreement.", "Sed id pendet, inquit Trump, ex eō an Īrānia pactum firmissimum signet.")
pl("The blockade remains. Iran is under pressure.", "Obsidiō manet. Īrānia premitur.")

# ---------------- world 2: US ----------------
en("America. This week the House may vote to impeach War Secretary Hegseth, and Mississippi's postal votes close today.")
pl("Now the United States of America.", "Nunc Cīvitātēs Foederātae Americae.")
pl("Yesterday we said: Thomas Massie, a Republican, wants to impeach Hegseth, the Secretary of War.", "Herī dīximus: Thomas Massie, Rēpūblicānus, Hegseth, ministrum bellī, accūsāre vult.")
pl("Today: perhaps this very week the House of Representatives will vote.", "Hodiē: fortasse hāc ipsā hebdomade Domus Repraesentantium suffrāgium feret.")
pl("Hakeem Jeffries leads the Democrats in the House.", "Hakeem Jeffries Dēmocratās in Domō Repraesentantium dūcit.")
pl("Jeffries says: Hegseth has got to go.", "Jeffries dīcit: Hegseth discēdere dēbet.")
pl("Hegseth has said: this did not work against Trump, and it will not work against me.", "Hegseth dīxit: hoc nōn valuit contrā Trump, nec valēbit contrā mē.")
pl("Today in America the Republicans in Congress are choosing their leaders.", "Hodiē in Americā Rēpūblicānī in Congressū ducēs suōs legunt.")
pl("Yesterday we said: two Senate seats are still undecided.", "Herī dīximus: duae sēdēs senātūs adhūc incertae sunt.")
pl("In Mississippi Scott Colom is narrowly ahead: by 2,574 votes.", "In Mississippiā Scott Colom paulum superat: duōbus mīlibus quīngentīs septuāgintā quattuor suffrāgiīs.")
pl("Postal votes are accepted until today, the 10th of November.", "Epistulae cum suffrāgiīs usque ad hodiernum diem, decimum Novembris, accipiuntur.")
pl("Cindy Hyde-Smith, the Republican senator, says: we are not backing down.", "Cindy Hyde-Smith, senātrīx Rēpūblicāna, dīcit: nōn cēdimus.")
pl("In Alaska, if no one has half the votes, a new count begins on the 18th of November.", "In Alaskā, sī nēmō dīmidium suffrāgiōrum habet, numerātiō nova incipit diē duodēvīcēsimō Novembris.")
pl("And Vice President Vance says: the reason we lost is the war.", "Et Vance, vicārius praesidis, dīcit: causa clādis nostrae est bellum.")

# ---------------- world 3: Ukraine ----------------
en("Ukraine. Peace talks begin today in Abu Dhabi, after a weekend of strikes on the power grid.")
pl("Now Ukraine.", "Nunc Ūcraīna.")
pl("Yesterday we said: new talks on peace are being prepared in the city of Abu Dhabi.", "Herī dīximus: novī sermōnēs dē pāce in urbe Abu Dhabi parantur.")
pl("Today the talks begin. They last two days, today and tomorrow.", "Hodiē sermōnēs incipiunt. Duōs diēs dūrant, hodiē et crās.")
pl("The Americans lead the talks: Steve Witkoff and Jared Kushner.", "Americānī sermōnēs dūcunt: Stephanus Witkoff et Iared Kushner.")
pl("Rustem Umerov will lead the Ukrainian delegation.", "Rustem Umerov lēgātiōnem Ūcraīnam dūcet.")
pl("They will speak about the end of the war, and about security after the war.", "Dē fīne bellī loquentur, et dē sēcūritāte post bellum.")
pl("But before the talks the Russians attacked again.", "Sed ante sermōnēs Russī iterum oppugnāvērunt.")
pl("The Russians say: we hit four electrical stations.", "Russī dīcunt: quattuor stātiōnēs ēlectricās percussimus.")
pl("In October, in Kyiv, 600,000 people were without light.", "Mēnse Octōbrī, Kioviae, sescenta mīlia hominum sine lūce erant.")
pl("Winter is coming, and the Russians want to take away light and heat.", "Hiems venit, et Russī lūcem et calōrem auferre volunt.")
pl("Zelensky says: Europe will give money faster to repair the power stations.", "Zelensky dīcit: Eurōpa pecūniam celerius dabit ad stātiōnēs reficiendās.")
pl("And today the Security Council of the United Nations is speaking about Ukraine.", "Et hodiē Cōnsilium Sēcūritātis Nātiōnum Ūnītārum dē Ūcraīnā loquitur.")
pl("Talks in the city of Abu Dhabi, but the war goes on.", "Sermōnēs in urbe Abu Dhabi, sed bellum pergit.")

# ---------------- good news ----------------
en("Something good. In Flint, Michigan, mothers get cash support, and the number of newborn babies who die has halved.")
spl("Good news.", "Rēs laeta.")
pl("Flint is a city in America, in Michigan.", "Flint urbs est in Americā, in Michigania.")
pl("In the city of Flint many families are poor.", "In urbe Flint multae familiae pauperēs sunt.")
pl("There, mothers receive money, before the birth and after.", "Ibi mātrēs pecūniam accipiunt, ante partum et post.")
pl("The programme is called Rx Kids.", "Hoc cōnsilium Rx Kids vocātur.")
pl("And now the good news: fewer newborn babies are dying.", "Et nunc rēs laeta: pauciōrēs īnfantēs novī moriuntur.")
pl("The deaths of newborn babies have fallen by half.", "Mortēs īnfantium novōrum dīmidiō cecidērunt.")
pl("Before, about 10 babies in a thousand died. Now about 5.", "Anteā circiter decem īnfantēs ex mīlle moriēbantur. Nunc circiter quīnque.")
pl("Mothers receive money, and babies live.", "Mātrēs pecūniam accipiunt, et īnfantēs vīvunt.")
pl("A poor city, a great work.", "Pauper urbs, magnum opus.")

# ---------------- opinion ----------------
en("Opinion. This is the view of David Flint, in The Spectator Australia: Australians have given up on Anthony Albanese.")
spl("Opinion.", "Opīniō.")
pl("This is the view of David Flint, in The Spectator Australia.", "Haec est sententia David Flint, in Spectātōre Austrāliānō.")
pl("Flint says: Australians have given up on Albanese.", "Flint dīcit: Austrāliānī Albanēsium dēseruērunt.")
pl("Australians no longer trust Albanese.", "Austrāliānī Albanēsiō fidem iam nōn habent.")
pl("Flint says: Albanese shows a new low in accountability.", "Flint dīcit: Albanese novum īmum gradum in ratiōne reddendā ostendit.")
pl("Flint sees two things against Labor.", "Flint duās rēs contrā Labōrānōs videt.")
pl("First: the voters have given up on Albanese.", "Prīmum: cīvēs Albanēsium dēseruērunt.")
pl("Second: many patriotic Australians now prefer One Nation, the party of Pauline Hanson.", "Deinde: multī Austrāliānī quī patriam amant nunc Ūnam Nātiōnem, factiōnem Paulīnae Hanson, praeferunt.")
pl("And Taylor and Canavan, as Flint says, have become steadfast leaders, who keep the old ways.", "Et Taylor et Canavan, ut Flint dīcit, ducēs cōnstantēs factī sunt, quī mōrēs antīquōs servant.")
pl("Flint says: no wonder Australians are giving up on him.", "Flint dīcit: nōn mīrum est Austrāliānōs eum dēserere.")
pl("That is the opinion of David Flint.", "Haec est opīniō David Flint.")

# ---------------- on this day ----------------
en("On this day, in the year four hundred and sixty-one, Pope Leo the Great died in Rome.")
spl("Today in history.", "Hodiē in historiā.")
pl("Today, in the year 461, Pope Leo the Great died, in Rome.", "Hodiē, annō quadringentēsimō sexāgēsimō prīmō, Pāpa Leō Magnus Rōmae mortuus est.")
pl("In the year 452 Attila, king of the Huns, came into Italy.", "Annō quadringentēsimō quīnquāgēsimō secundō Attila, rēx Hunnōrum, in Italiam vēnit.")
pl("Leo went to Attila, near Lake Garda.", "Leō ad Attilam iit, prope lacum Bēnācum.")
pl("Leo spoke with Attila. And Attila went back.", "Leō cum Attilā locūtus est. Et Attila rediit.")
pl("He was the first pope to be called the Great.", "Prīmus Pāpa fuit quī Magnus vocātus est.")
pl("Today the Church celebrates his feast day.", "Hodiē Ecclēsia diem fēstum eius celebrat.")
pl("Marcus and Lucius, as always, were there. But that is another story.", "Mārcus et Lūcius, ut semper, aderant. Sed id alia fābula est.")

# ---------------- summary ----------------
en("The day in brief.")
spl("Summary of the news.", "Summa rērum.")
pl("In Canberra today fog in the morning, then 25 degrees.", "Canberrae hodiē māne nebula, deinde quīnque et vīgintī gradūs.")
pl("Tomorrow it will be warmer: 28 degrees, and perhaps a shower.", "Crās calidius erit: duodētrīgintā gradūs, et fortasse imber.")
pl("Inflation in Australia is high: 4.3 per cent.", "Īnflātiō in Austrāliā alta est: quattuor et trēs decimae per centum.")
pl("Colleagues are leaking secrets against Chalmers.", "Collēgae sēcrēta contrā Chalmers prōdunt.")
pl("Only one in five Australians trusts Albanese.", "Ūnus tantum ē quīnque Austrāliānīs Albanēsiō fidem habet.")
pl("Trump says: almost nothing gets into Iran, or out of Iran.", "Trump dīcit: paene nihil in Īrāniam intrat, aut ex Īrāniā exit.")
pl("Rubio says: Iran's proposal is ridiculous.", "Rubio dīcit: prōpositum Īrāniae rīdiculum est.")
pl("Perhaps this week the House of Representatives will vote on Hegseth.", "Fortasse hāc hebdomade Domus Repraesentantium dē Hegseth suffrāgium feret.")
pl("In Mississippi postal votes are accepted until today.", "In Mississippiā epistulae cum suffrāgiīs usque ad hodiernum diem accipiuntur.")
pl("Today the talks on peace begin in the city of Abu Dhabi.", "Hodiē sermōnēs dē pāce in urbe Abu Dhabi incipiunt.")
pl("In the city of Flint fewer newborn babies are dying.", "In urbe Flint pauciōrēs īnfantēs novī moriuntur.")
pl("Flint says: Australians have given up on Albanese.", "Flint dīcit: Austrāliānī Albanēsium dēseruērunt.")
pl("And today Pope Leo the Great died.", "Et hodiē Pāpa Leō Magnus mortuus est.")

# ---------------- words of the day ----------------
en("The words of the day. Five sentences, slowly.")
spl("The words of the day.", "Verba diēī.")
pl("Colleagues are leaking secrets against Chalmers.", "Collēgae sēcrēta contrā Chalmers prōdunt.")
pl("Only one in five trusts Albanese.", "Ūnus tantum ē quīnque Albanēsiō fidem habet.")
pl("Almost nothing gets into Iran, or out of Iran.", "Paene nihil in Īrāniam intrat, aut ex Īrāniā exit.")
pl("Today the talks on peace begin.", "Hodiē sermōnēs dē pāce incipiunt.")
pl("Mothers receive money, and fewer babies die.", "Mātrēs pecūniam accipiunt, et pauciōrēs īnfantēs moriuntur.")
pl("Again.", "Iterum.")
pl("Colleagues are leaking secrets against Chalmers.", "Collēgae sēcrēta contrā Chalmers prōdunt.")
pl("Only one in five trusts Albanese.", "Ūnus tantum ē quīnque Albanēsiō fidem habet.")
pl("Almost nothing gets into Iran, or out of Iran.", "Paene nihil in Īrāniam intrat, aut ex Īrāniā exit.")
pl("Today the talks on peace begin.", "Hodiē sermōnēs dē pāce incipiunt.")
pl("Mothers receive money, and fewer babies die.", "Mātrēs pecūniam accipiunt, et pauciōrēs īnfantēs moriuntur.")
pl("This is the Acta Diurna. Goodbye, listeners. Again tomorrow.", "Haec sunt Ācta Diurna. Valēte, audītōrēs. Crās iterum.")
p1pl("Now everything again, in Latin only.", "Nunc omnia iterum, Latīnē tantum.")

job = {
 "type": "news", "date": "2026-11-10", "music": "v5",
 "title": "Ācta Diurna · Diēs Mārtis, IV Īd. Nov. (Tue 10 Nov 2026)",
 "summary": ("Canberra: fog, then 4–25° and mostly sunny; 28° and a chance of storms tomorrow. Australia: inflation 4.3%, "
             "Murray Watt tells colleagues to stop leaking against Chalmers, $3bn over-65s rebate cut stuck in the Senate, "
             "Resolve: only 20% trust Albanese, Taylor: 'out of touch, out of his depth'. Iran: Trump says Iron Gate is in full force, "
             "'very little gets into, or out of, Iran'; Rubio calls Iran's offer 'outrageous and ridiculous'. US: House may vote "
             "to impeach Hegseth this week, Jeffries: 'Hegseth has got to go'; Mississippi postal votes close today. Ukraine: "
             "US-brokered talks open in Abu Dhabi after strikes on the grid. Flint, Michigan: newborn deaths halve under Rx Kids. "
             "Opīniō: David Flint, 'Australians have given up on Albanese'. Pope Leo the Great died, AD 461. "
             "Every line in English, then Latin; then all the Latin again. Sources: Bureau of Meteorology; ABC News (9 Nov); "
             "The Age/SMH (9 Nov); The National and Al Jazeera (9 Nov); Just Security (9 Nov); Roll Call (9 Nov); Yahoo News (7 Nov); "
             "UN News (9 Nov); Reuters (2 Nov); Good Good Good (7 Nov); The Spectator Australia (David Flint, 31 Oct)."),
 "lines": L,
}
if __name__ == "__main__":
    json.dump(job, open("jobs/0068-news-2026-11-10.json", "w"), ensure_ascii=False, indent=1)
    lat = [r[-1] for k, *r in L if k != 'en']
    w = sum(len(t.split()) for t in lat)
    import re
    bad = [t for t in lat if re.search(r'\d', t)]
    print(len(L), 'lines ·', len(lat), 'Latin lines ·', w, 'Latin words · digits:', bad)
