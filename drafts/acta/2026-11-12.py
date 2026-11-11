# Ex Ōre Equī · Thursday 12 November 2026. Free voices (Jenny + Paola). English → Latin on every line, then all the Latin again.
# First horse episode (HORSE RULE, 11 Nov 2026).
# Sources (read 12 Nov 2026, early morning, Canberra): Bureau of Meteorology place forecasts (issued 11 Nov) · ABC News business live 11 Nov
# (ABS home loans, David Jones, CBA, ANZ) · The Spectator Australia: Michael de Percy, 10 Nov · Al Jazeera 11 Nov, The Week 10 Nov,
# Just Security 11 Nov (Rubio, Trump, Rezaei) · Al Jazeera 11 Nov (Hegseth vote) · Moscow Times, Kyiv Post, AP via KRMG, Reuters via Yahoo
# 11 Nov (Abu Dhabi talks) · Good News Network 10 Nov (Roman Heilman found) · Wikipedia: St Josaphat Kuntsevych.
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
pl("Today is Thursday, the day before the Ides of November.", "Hodiē est diēs Iovis, prīdiē Īdūs Novembrēs.")
pl("In the year 2026.", "Annō bis mīllēsimō vīcēsimō sextō.")
pl("First, the weather. Then Australian affairs.", "Prīmum tempestās. Deinde rēs Austrāliae.")
pl("Then the world: Iran, America, Ukraine.", "Deinde orbis terrārum: Īrānia, America, Ūcraīna.")
pl("Then a happy story, opinion, and today in history.", "Tum rēs laeta, opīniō, et hodiē in historiā.")
pl("At the end, the words of the day.", "In fīne, verba diēī.")

# ---------------- weather ----------------
en("The weather. Canberra: fog early, then mostly sunny, 27 degrees. Tomorrow 30, and perhaps thunder.")
spl("The weather.", "Tempestās.")
pl("First, Canberra.", "Prīmum Canberra.")
pl("Yesterday we said: tomorrow morning perhaps fog, then 27 degrees.", "Herī dīximus: crās māne fortasse nebula, deinde septem et vīgintī gradūs.")
pl("And so it is. Today in Canberra, in the morning, perhaps fog.", "Et ita est. Hodiē Canberrae, māne, fortasse nebula.")
pl("Then the sun is shining. The sky is mostly clear.", "Deinde sōl lūcet. Caelum ferē serēnum est.")
pl("In the morning it is cool: 10 degrees.", "Māne frīgidum est: decem gradūs.")
pl("In the afternoon it is warm: 27 degrees.", "Post merīdiem calidum est: septem et vīgintī gradūs.")
pl("The wind blows from the east, 15 to 25 kilometres an hour.", "Ventus ab oriente flat, quīndecim ad vīgintī quīnque chiliometra in hōrā.")
pl("Good news for the grass. The grass in Canberra is green and sweet.", "Bonum nūntium herbae. Herba Canberrae viridis et dulcis est.")
pl("Tomorrow, Friday, the sky will be partly cloudy.", "Crās, diē Veneris, caelum partim nūbilum erit.")
pl("Tomorrow morning 11 degrees, in the afternoon 30.", "Crās māne ūndecim gradūs, post merīdiem trīgintā.")
pl("Tomorrow, in the afternoon, perhaps a shower, perhaps thunder.", "Crās, post merīdiem, fortasse imber, fortasse tonitrus.")
pl("When there is thunder, a wise animal stays in the stable.", "Ubi tonitrus est, sapiēns animal in stabulō manet.")
pl("So: today 27 degrees, tomorrow 30.", "Ergō: hodiē septem et vīgintī gradūs, crās trīgintā.")
pl("Now the other cities.", "Nunc cēterae urbēs.")
pl("In Sydney the sky is partly cloudy. Perhaps a shower. 24 degrees.", "Sydnēiae caelum partim nūbilum est. Fortasse imber. Quattuor et vīgintī gradūs.")
pl("In Melbourne the sun is shining. 21 degrees.", "Melburnī sōl lūcet. Ūnus et vīgintī gradūs.")
pl("In Brisbane thunder is likely. 31 degrees.", "Brisbanae tonitrus probābilis est. Ūnus et trīgintā gradūs.")
pl("In Perth the sun is shining. 27 degrees.", "Perthī sōl lūcet. Septem et vīgintī gradūs.")
pl("In Adelaide the sun is shining. 25 degrees.", "Adēlāidae sōl lūcet. Quīnque et vīgintī gradūs.")
pl("In Hobart the sun is shining. 24 degrees.", "Hobartī sōl lūcet. Quattuor et vīgintī gradūs.")
pl("Sun almost everywhere. A fine day for the grass, and for those who eat it.", "Sōl ferē ubīque. Diēs pulcher herbae, et eīs quī eam edunt.")
pl("That is the weather.", "Haec est tempestās.")

# ---------------- Australia ----------------
en("Australia. New home loans fell 15.5 per cent: the biggest fall on record. Investors fell by a third. David Jones will close 19 stores.")
spl("Australian affairs.", "Rēs Austrāliae.")
pl("Yesterday we said: Albanese flew to Turkey.", "Herī dīximus: Albanese in Turciam volāvit.")
pl("And Taylor says: the Prime Minister and this government have wrecked the economy.", "Et Taylor dīcit: prīmus minister et haec rēs pūblica oeconomiam perdidērunt.")
pl("Today new numbers about the economy.", "Hodiē novī numerī dē oeconomiā.")
pl("Australians are borrowing much less money to buy houses.", "Austrāliānī multō minus pecūniae mūtuantur ut domōs emant.")
pl("New loans for houses fell 15 and a half per cent, in three months.", "Nova mūtua prō domibus cecidērunt quīndecim per centum et dīmidium, tribus mēnsibus.")
pl("Never before have loans for houses fallen so much.", "Numquam anteā mūtua prō domibus tantum cecidērunt.")
pl("Investors are those who buy houses to rent them out.", "Collocātōrēs sunt eī quī domōs emunt ut eās locent.")
pl("Loans to investors fell by more than 32 per cent.", "Mūtua collocātōribus cecidērunt plūs quam trīgintā duo per centum.")
pl("Why? A bank economist, Tom Ryan, says: because of the new taxes in the budget.", "Cūr? Tom Ryan, perītus argentāriae, dīcit: propter nova tribūta in ratiōne pūblicā.")
pl("New taxes on houses for investors. So investors buy less.", "Nova tribūta in domōs collocātōrum. Itaque collocātōrēs minus emunt.")
pl("The interest rate is high, and the hay is dear.", "Faenus altum est, et faenum cārum est.")
pl("Faenus and faenum: one letter different, both too expensive.", "Faenus et faenum: ūna littera differt, utrumque nimis cārum.")
pl("And the great store David Jones will close 19 stores, about half.", "Et magna taberna David Jones ūndēvīgintī tabernās claudet, circiter dīmidium.")
pl("Nineteen stores will close. About stables, nothing was said.", "Ūndēvīgintī tabernae claudentur. Dē stabulīs nihil dictum est.")
pl("The biggest bank, CBA, made a profit of almost 3 billion dollars in three months.", "Maxima argentāria, CBA, tribus mēnsibus lucrum fēcit paene tria mīlliarda dollarōrum.")
pl("But its chief, Matt Comyn, says: higher inflation and interest rates continue to put uneven pressure on households and businesses.", "Sed prīnceps eius, Matt Comyn, dīcit: īnflātiō altior et faenora altiōra familiās et negōtia adhūc inaequāliter premunt.")
pl("Fewer loans, new taxes, stores closing.", "Pauciōra mūtua, nova tribūta, tabernae clausae.")
pl("That is the state of Australia today.", "Haec est rēs Austrāliae hodiē.")

# ---------------- world 1: Iran ----------------
en("The world. Iran: Rubio says the economic pressure is so strong that there is no need for big battles. Iran says: not one particle of uranium will leave.")
spl("The world.", "Orbis terrārum.")
pl("First, Iran.", "Prīmum Īrānia.")
pl("Yesterday we said: Trump says: the war with Iran is effectively over.", "Herī dīximus: Trump dīcit: bellum cum Īrāniā paene cōnfectum est.")
pl("But if we must go back, we are ready.", "Sed sī redīre dēbēmus, parātī sumus.")
pl("Today Marco Rubio, the Secretary of State, speaks.", "Hodiē Mārcus Rubio, minister rērum externārum, loquitur.")
pl("Rubio says: the economic war is so heavy that there is no need for great battles.", "Rubio dīcit: bellum oeconomicum tam grave est ut magnīs proeliīs nōn sit opus.")
pl("No cavalry charge is needed. The oats are simply taken away.", "Nūllō equitātū opus est. Avēna tantum aufertur.")
pl("And Trump says: new strikes are quite unlikely.", "Et Trump dīcit: novī ictūs haud probābilēs sunt.")
pl("The blockade remains, by land and by sea.", "Obsidiō manet, terrā et marī.")
pl("Yesterday we said: Iran still demands seven conditions.", "Herī dīximus: Īrānia adhūc septem condiciōnēs postulat.")
pl("Rubio says: Iran's demands are totally unrealistic.", "Rubio dīcit: postulāta Īrāniae omnīnō vāna sunt.")
pl("Today Mohsen Rezaei says: not even one particle of uranium will leave Iran.", "Hodiē Mohsen Rezaei dīcit: nē ūna quidem particula ūraniī Īrāniam relinquet.")
pl("Not even one particle. We counted the particles. It took all night.", "Nē ūna quidem particula. Particulās numerāvimus. Tōtam noctem.")
pl("And Rezaei says: if America attacks, we will strike American bases far away.", "Et Rezaei dīcit: sī America oppugnāverit, castra Americāna longinqua feriēmus.")
pl("No great battles, but the blockade remains.", "Nūlla magna proelia, sed obsidiō manet.")

# ---------------- world 2: US ----------------
en("America. The House voted 211 to 204 to send Massie's charges against Hegseth back to committee. Eleven Democrats were absent; some blamed the traffic.")
pl("Now the United States of America.", "Nunc Cīvitātēs Foederātae Americae.")
pl("Yesterday we said: today the House of Representatives votes on Hegseth.", "Herī dīximus: hodiē Domus Repraesentantium dē Hegseth suffrāgium fert.")
pl("And Hegseth says: it is a political spectacle.", "Et Hegseth dīcit: spectāculum polīticum est.")
pl("The House has voted. 211 votes against 204.", "Domus suffrāgium tulit. Ducenta ūndecim suffrāgia contrā ducenta quattuor.")
pl("Almost a photo finish, as on the racecourse.", "Paene pār fīnis, ut in curriculō.")
pl("The House sent the charges back to a committee.", "Domus crīmina ad commissiōnem remīsit.")
pl("Massie says: this was a way to kill the plan.", "Massie dīcit: hic erat modus cōnsilium exstinguendī.")
pl("Massie was the only Republican who voted against.", "Massie sōlus ē Rēpūblicānīs contrā suffrāgium tulit.")
pl("But eleven Democrats were absent.", "Sed ūndecim Dēmocratae aberant.")
pl("If they had been there, the charges would not have been sent back.", "Sī adfuissent, crīmina nōn remissa essent.")
pl("Four Democrats say that they were held up in the traffic.", "Quattuor Dēmocratae dīcunt sē in viīs tardōs fuisse.")
pl("Eleven absent. Four in the traffic. The great war of impeachment, lost in the traffic.", "Ūndecim absentēs. Quattuor in viīs. Magnum bellum accūsātiōnis in viīs āmissum.")
pl("A lesson: in the city, a good horse is never late.", "Documentum: in urbe, bonus equus numquam tardus est.")
pl("Trump says: the Democrats' attempt has miserably failed!", "Trump dīcit: cōnātus Dēmocratārum miserē dēfēcit!")
pl("But on the 3rd of January the Democrats will rule the House.", "Sed diē tertiō mēnsis Iānuāriī Dēmocratae Domum regent.")
pl("Then perhaps the charges will come back.", "Tum fortasse crīmina redībunt.")

# ---------------- world 3: Ukraine ----------------
en("Ukraine. The Abu Dhabi talks ended after two days, with no breakthrough. A prisoner exchange of a thousand for a thousand is being discussed.")
pl("Now Ukraine.", "Nunc Ūcraīna.")
pl("Yesterday we said: in the city of Abu Dhabi the talks have begun. The Ukrainians want a ceasefire.", "Herī dīximus: in urbe Abu Dhabi sermōnēs coepērunt. Ūcraīnī indūtiās volunt.")
pl("Today: the talks have ended, after two days.", "Hodiē: sermōnēs fīnītī sunt, post duōs diēs.")
pl("Jared Kushner says: we are encouraged by the constructive talks.", "Iared Kushner dīcit: sermōnibus ūtilibus cōnfirmātī sumus.")
pl("Zelensky says: the talks were constructive and quite substantial.", "Zelensky dīcit: sermōnēs ūtilēs et satis gravēs fuērunt.")
pl("But there is no peace yet, and no ceasefire.", "Sed nūlla pāx adhūc est, nūllae indūtiae.")
pl("The Russians still demand the whole of the Donbas.", "Russī adhūc tōtum Donbassum postulant.")
pl("Zelensky refuses to give up the land.", "Zelensky terram trādere recūsat.")
pl("They discussed prisoners: perhaps a thousand for a thousand.", "Dē captīvīs disseruērunt: fortasse mīlle prō mīlle.")
pl("A thousand prisoners for a thousand prisoners. A fair exchange, like a horseshoe for a horseshoe.", "Mīlle captīvī prō mīlle captīvīs. Aequa permūtātiō, ut solea prō soleā.")
pl("And the war goes on. The Russians say: in one night we brought down 627 Ukrainian drones.", "Et bellum pergit. Russī dīcunt: ūnā nocte sescentōs vīgintī septem fūcōs Ūcraīnōs dēiēcimus.")
pl("Talks ended, prisoners discussed, drones in the night.", "Sermōnēs fīnītī, dē captīvīs disputātum, fūcī noctū.")

# ---------------- good news ----------------
en("Something good. In Kentucky, a six-year-old boy with autism, missing for three days, was found alive by a man of a horse-riding group.")
spl("Good news.", "Rēs laeta.")
pl("In America, in Kentucky, near West Virginia, there is a boy named Roman.", "In Americā, in Kentuckiā, prope Virginiam Occidentālem, est puer nōmine Rōmānus.")
pl("He is six years old. He has autism.", "Sex annōs nātus est. Autismum habet.")
pl("On Sunday, the first of November, he went missing in the woods.", "Diē Sōlis, Kalendīs Novembribus, in silvīs āmissus est.")
pl("Very many people searched for him: on foot, with drones, and on horseback.", "Permultī hominēs eum quaesīvērunt: pedibus, fūcīs, et equīs.")
pl("He spent two cold nights in the woods.", "Duās noctēs frīgidās in silvīs ēgit.")
pl("Jacob Mullins, from a horse-riding group, found him.", "Iacōbus Mullins, ex societāte equitum, eum invēnit.")
pl("Mullins says: he just walked right out of the bushes onto a horse trail.", "Mullins dīcit: ex dūmīs in sēmitam equōrum simpliciter exiit.")
pl("Roman was scratched, but alive. A small dog was following him.", "Rōmānus vulnerātus leviter, sed vīvus erat. Parvus canis eum sequēbātur.")
pl("And he was singing a song about a farm.", "Et carmen dē fundō canēbat.")
pl("Found on a horse trail, by a horseman. We add nothing. We are simply proud.", "Inventus in sēmitā equōrum, ab equite. Nihil addimus. Superbī tantum sumus.")

# ---------------- opinion ----------------
en("Opinion. This is the view of Michael de Percy, in The Spectator Australia: Albanese is sleepwalking Australia into poverty, like France.")
spl("Opinion.", "Opīniō.")
pl("This is the view of Michael de Percy, in The Spectator Australia.", "Haec est sententia Michael de Percy, in Spectātōre Austrāliānō.")
pl("De Percy says: Anthony Albanese is sleepwalking Australia into poverty.", "De Percy dīcit: Antōnius Albanese Austrāliam dormiēns in paupertātem dūcit.")
pl("Look at France, he says. Since 1974 France has never had a balanced budget.", "Spectāte Galliam, inquit. Ab annō mīllēsimō nōngentēsimō septuāgēsimō quārtō Gallia ratiōnem pūblicam numquam aequāvit.")
pl("And work is producing less: productivity is falling.", "Et opus minus efficit: frūctus labōris cadit.")
pl("Inflation is high, as de Percy says.", "Īnflātiō alta est, ut de Percy dīcit.")
pl("De Percy also blames the Coalition, which in the past did not dare to save.", "De Percy etiam Coalitiōnem culpat, quae ōlim parcere nōn ausa est.")
pl("A horse sleeps standing up. But at least he does not walk.", "Equus stāns dormit. Sed saltem nōn ambulat.")
pl("That is the opinion of Michael de Percy.", "Haec est opīniō Michael de Percy.")

# ---------------- on this day ----------------
en("On this day in 1623 Saint Josaphat, archbishop of Polotsk, born in what is now Ukraine, was killed in Vitebsk for working for union with Rome.")
spl("Today in history.", "Hodiē in historiā.")
pl("Today the Church celebrates the feast of Saint Josaphat.", "Hodiē Ecclēsia fēstum sānctī Iōsaphat celebrat.")
pl("Josaphat was born about the year 1580, in Volodymyr, in what is now Ukraine.", "Iōsaphat nātus est circiter annō mīllēsimō quīngentēsimō octōgēsimō, in oppidō Volodymyr, in terrā quae nunc Ūcraīna est.")
pl("He became archbishop of Polotsk.", "Archiepiscopus Polociae factus est.")
pl("He worked for the union of the Ruthenian Church with Rome.", "Prō ūniōne Ecclēsiae Ruthēnae cum Rōmā labōrāvit.")
pl("Today, in the year 1623, in the city of Vitebsk, an angry crowd attacked his house.", "Hodiē, annō mīllēsimō sescentēsimō vīcēsimō tertiō, in urbe Vitebsk, turba īrāta domum eius oppugnāvit.")
pl("They killed him with an axe, and threw his body into the river Dvina.", "Eum secūrī occīdērunt, et corpus eius in flūmen Dūnam iēcērunt.")
pl("In 1867 the Pope made him a saint. Today his body lies in Saint Peter's, in Rome.", "Annō mīllēsimō octingentēsimō sexāgēsimō septimō Pāpa eum sānctum fēcit. Hodiē corpus eius in basilicā sānctī Petrī, Rōmae, iacet.")
pl("On this day, by the way, no horse was made consul. We checked twice.", "Hodiē, obiter, nūllus equus cōnsul factus est. Bis quaesīvimus.")
pl("Marcus and Lucius, as always, were there. But that is another story.", "Mārcus et Lūcius, ut semper, aderant. Sed id alia fābula est.")

# ---------------- summary ----------------
en("The day in brief.")
spl("Summary of the news.", "Summa rērum.")
pl("In Canberra today 27 degrees, and the sun is shining.", "Canberrae hodiē septem et vīgintī gradūs, et sōl lūcet.")
pl("New loans for houses fell 15 and a half per cent. Never before so much.", "Nova mūtua prō domibus cecidērunt quīndecim per centum et dīmidium. Numquam anteā tantum.")
pl("Loans to investors fell by more than 32 per cent, because of the new taxes.", "Mūtua collocātōribus cecidērunt plūs quam trīgintā duo per centum, propter nova tribūta.")
pl("David Jones will close 19 stores.", "David Jones ūndēvīgintī tabernās claudet.")
pl("Rubio says: there is no need for great battles. The blockade remains.", "Rubio dīcit: magnīs proeliīs nōn est opus. Obsidiō manet.")
pl("The House sent the charges against Hegseth back to a committee. 211 against 204.", "Domus crīmina contrā Hegseth ad commissiōnem remīsit. Ducenta ūndecim contrā ducenta quattuor.")
pl("Eleven Democrats were absent. Four were in the traffic.", "Ūndecim Dēmocratae aberant. Quattuor in viīs erant.")
pl("In the city of Abu Dhabi the talks have ended. No peace yet.", "In urbe Abu Dhabi sermōnēs fīnītī sunt. Nūlla pāx adhūc.")
pl("Perhaps a thousand prisoners for a thousand.", "Fortasse mīlle captīvī prō mīlle.")
pl("In Kentucky, a horseman found the boy Roman, alive.", "In Kentuckiā eques puerum Rōmānum vīvum invēnit.")

# ---------------- words of the day ----------------
en("The words of the day. Five sentences, slowly.")
spl("The words of the day.", "Verba diēī.")
pl("New loans for houses fell; the investors buy less.", "Nova mūtua prō domibus cecidērunt; collocātōrēs minus emunt.")
pl("The interest rate is high, and the hay is dear.", "Faenus altum est, et faenum cārum est.")
pl("No cavalry charge is needed. The oats are simply taken away.", "Nūllō equitātū opus est. Avēna tantum aufertur.")
pl("The House sent the charges back to a committee.", "Domus crīmina ad commissiōnem remīsit.")
pl("A thousand prisoners for a thousand prisoners.", "Mīlle captīvī prō mīlle captīvīs.")
pl("Again.", "Iterum.")
pl("New loans for houses fell; the investors buy less.", "Nova mūtua prō domibus cecidērunt; collocātōrēs minus emunt.")
pl("The interest rate is high, and the hay is dear.", "Faenus altum est, et faenum cārum est.")
pl("No cavalry charge is needed. The oats are simply taken away.", "Nūllō equitātū opus est. Avēna tantum aufertur.")
pl("The House sent the charges back to a committee.", "Domus crīmina ad commissiōnem remīsit.")
pl("A thousand prisoners for a thousand prisoners.", "Mīlle captīvī prō mīlle captīvīs.")
pl("That was the news, straight from the horse's mouth. Goodbye, listeners. Again tomorrow.", "Haec fuērunt nūntia ex ōre equī. Valēte, audītōrēs. Crās iterum.")
p1pl("Now everything again, in Latin only.", "Nunc omnia iterum, Latīnē tantum.")

job = {
 "type": "news", "date": "2026-11-12", "suffix": "-r", "music": "v5",
 "title": "Ex Ōre Equī · Diēs Iovis, prīd. Īd. Nov. (Thu 12 Nov 2026)",
 "summary": ("Canberra: 10–27°, early fog then mostly sunny; 11–30° and a storm chance tomorrow; Brisbane storms, 31°. "
             "Australia: new home loans fall 15.5% in the September quarter, the biggest fall on record; investor lending down 32.3% "
             "(J.P. Morgan: budget tax changes); David Jones to close 19 stores; CBA quarterly profit A$2.8bn, Comyn on pressure from "
             "inflation and rates; Iran: Rubio: 'no need for major combat operations', Iran's demands "
             "'totally unrealistic'; Trump: new strikes 'quite unlikely'; Rezaei: not 'a single particle' of enriched material will leave Iran. "
             "US: House votes 211–204 to send Massie's Hegseth impeachment articles back to committee; 11 Democrats absent; Trump: 'miserably "
             "FAILED!'. Ukraine: Abu Dhabi talks end after two days with no breakthrough; prisoner swap of 1,000 for 1,000 discussed. "
             "Kentucky: six-year-old Roman Heilman found alive by a trail rider after three days. Opīniō: Michael de Percy, Albanese is "
             "'sleepwalking Australia into systemic poverty'. St Josaphat, killed in Vitebsk, 12 Nov 1623. Every line in English, then Latin; "
             "then all the Latin again. Sources: Bureau of Meteorology; ABC News (11 Nov); The Spectator Australia (Michael de Percy, 10 Nov); "
             "Al Jazeera (11 Nov); The Week (10 Nov); Just Security (11 Nov); The Moscow Times, Kyiv Post, AP, Reuters (11 Nov); "
             "Good News Network (10 Nov); Wikipedia."),
 "lines": L,
}
if __name__ == "__main__":
    json.dump(job, open("jobs/0071-news-2026-11-12-r.json", "w"), ensure_ascii=False, indent=1)
    lat = [r[-1] for k, *r in L if k != 'en']
    w = sum(len(t.split()) for t in lat)
    import re
    bad = [t for t in lat if re.search(r'\d', t)]
    print(len(L), 'lines ·', len(lat), 'Latin lines ·', w, 'Latin words · digits:', bad)
