# Conjugaisons de base pour certains verbes à titre d'exemple
import random
from rich.console import Console

console = Console()


# Dictionnaire complet des conjugaisons pour chaque verbe et temps
conjugaisons = {
    'aimer': {
        'présent': ['j\' aime', 'tu aimes', 'il aime', 'nous aimons', 'vous aimez', 'ils aiment'],
        'passé composé': ['j\' ai aimé', 'tu as aimé', 'il a aimé', 'nous avons aimé', 'vous avez aimé', 'ils ont aimé'],
        'imparfait': ['j\' aimais', 'tu aimais', 'il aimait', 'nous aimions', 'vous aimiez', 'ils aimaient'],
        'futur simple': ['j\' aimerai', 'tu aimeras', 'il aimera', 'nous aimerons', 'vous aimerez', 'ils aimeront'],
        'conditionnel présent': ['j\' aimerais', 'tu aimerais', 'il aimerait', 'nous aimerions', 'vous aimeriez', 'ils aimeraient'],
        'passé simple': ['j\' aimai', 'tu aimas', 'il aima', 'nous aimâmes', 'vous aimâtes', 'ils aimèrent'],
        'plus que parfait': ['j\' avais aimé', 'tu avais aimé', 'il avait aimé', 'nous avions aimé', 'vous aviez aimé', 'ils avaient aimé'],
        'subjonctif présent': ['que j\' aime', 'que tu aimes', 'qu\' il aime', 'que nous aimions', 'que vous aimiez', 'qu\' ils aiment'],
        'conditionnel passé': ['j\' aurais aimé', 'tu aurais aimé', 'il aurait aimé', 'nous aurions aimé', 'vous auriez aimé', 'ils auraient aimé'],
        'futur antérieur': ['j\' aurai aimé', 'tu auras aimé', 'il aura aimé', 'nous aurons aimé', 'vous aurez aimé', 'ils auront aimé'],
    },
    'parler': {
        'présent': ['je parle', 'tu parles', 'il parle', 'nous parlons', 'vous parlez', 'ils parlent'],
        'passé composé': ['j\' ai parlé', 'tu as parlé', 'il a parlé', 'nous avons parlé', 'vous avez parlé', 'ils ont parlé'],
        'imparfait': ['je parlais', 'tu parlais', 'il parlait', 'nous parlions', 'vous parliez', 'ils parlaient'],
        'futur simple': ['je parlerai', 'tu parleras', 'il parlera', 'nous parlerons', 'vous parlerez', 'ils parleront'],
        'conditionnel présent': ['je parlerais', 'tu parlerais', 'il parlerait', 'nous parlerions', 'vous parleriez', 'ils parleraient'],
        'passé simple': ['je parlai', 'tu parlas', 'il parla', 'nous parlâmes', 'vous parlâtes', 'ils parlèrent'],
        'plus que parfait': ['j\' avais parlé', 'tu avais parlé', 'il avait parlé', 'nous avions parlé', 'vous aviez parlé', 'ils avaient parlé'],
        'subjonctif présent': ['que je parle', 'que tu parles', 'qu\' il parle', 'que nous parlions', 'que vous parliez', 'qu\' ils parlent'],
        'conditionnel passé': ['j\' aurais parlé', 'tu aurais parlé', 'il aurait parlé', 'nous aurions parlé', 'vous auriez parlé', 'ils auraient parlé'],
        'futur antérieur': ['j\' aurai parlé', 'tu auras parlé', 'il aura parlé', 'nous aurons parlé', 'vous aurez parlé', 'ils auront parlé'],
    },
    'donner': {
        'présent': ['je donne', 'tu donnes', 'il donne', 'nous donnons', 'vous donnez', 'ils donnent'],
        'passé composé': ['j\' ai donné', 'tu as donné', 'il a donné', 'nous avons donné', 'vous avez donné', 'ils ont donné'],
        'imparfait': ['je donnais', 'tu donnais', 'il donnait', 'nous donnions', 'vous donniez', 'ils donnaient'],
        'futur simple': ['je donnerai', 'tu donneras', 'il donnera', 'nous donnerons', 'vous donnerez', 'ils donneront'],
        'conditionnel présent': ['je donnerais', 'tu donnerais', 'il donnerait', 'nous donnerions', 'vous donneriez', 'ils donneraient'],
        'passé simple': ['je donnai', 'tu donnas', 'il donna', 'nous donnâmes', 'vous donnâtes', 'ils donnèrent'],
        'plus que parfait': ['j\' avais donné', 'tu avais donné', 'il avait donné', 'nous avions donné', 'vous aviez donné', 'ils avaient donné'],
        'subjonctif présent': ['que je donne', 'que tu donnes', 'qu\' il donne', 'que nous donnions', 'que vous donniez', 'qu\' ils donnent'],
        'conditionnel passé': ['j\' aurais donné', 'tu aurais donné', 'il aurait donné', 'nous aurions donné', 'vous auriez donné', 'ils auraient donné'],
        'futur antérieur': ['j\' aurai donné', 'tu auras donné', 'il aura donné', 'nous aurons donné', 'vous aurez donné', 'ils auront donné'],
    },
    'chanter': {
        'présent': ['je chante', 'tu chantes', 'il chante', 'nous chantons', 'vous chantez', 'ils chantent'],
        'passé composé': ['j\' ai chanté', 'tu as chanté', 'il a chanté', 'nous avons chanté', 'vous avez chanté', 'ils ont chanté'],
        'imparfait': ['je chantais', 'tu chantais', 'il chantait', 'nous chantions', 'vous chantiez', 'ils chantaient'],
        'futur simple': ['je chanterai', 'tu chanteras', 'il chantera', 'nous chanterons', 'vous chanterez', 'ils chanteront'],
        'conditionnel présent': ['je chanterais', 'tu chanterais', 'il chanterait', 'nous chanterions', 'vous chanteriez', 'ils chanteraient'],
        'passé simple': ['je chantai', 'tu chantas', 'il chanta', 'nous chantâmes', 'vous chantâtes', 'ils chantèrent'],
        'plus que parfait': ['j\' avais chanté', 'tu avais chanté', 'il avait chanté', 'nous avions chanté', 'vous aviez chanté', 'ils avaient chanté'],
        'subjonctif présent': ['que je chante', 'que tu chantes', 'qu\' il chante', 'que nous chantions', 'que vous chantiez', 'qu\' ils chantent'],
        'conditionnel passé': ['j\' aurais chanté', 'tu aurais chanté', 'il aurait chanté', 'nous aurions chanté', 'vous auriez chanté', 'ils auraient chanté'],
        'futur antérieur': ['j\' aurai chanté', 'tu auras chanté', 'il aura chanté', 'nous aurons chanté', 'vous aurez chanté', 'ils auront chanté'],
    },
    'jouer': {
        'présent': ['je joue', 'tu joues', 'il joue', 'nous jouons', 'vous jouez', 'ils jouent'],
        'passé composé': ['j\' ai joué', 'tu as joué', 'il a joué', 'nous avons joué', 'vous avez joué', 'ils ont joué'],
        'imparfait': ['je jouais', 'tu jouais', 'il jouait', 'nous jouions', 'vous jouiez', 'ils jouaient'],
        'futur simple': ['je jouerai', 'tu joueras', 'il jouera', 'nous jouerons', 'vous jouerez', 'ils joueront'],
        'conditionnel présent': ['je jouerais', 'tu jouerais', 'il jouerait', 'nous jouerions', 'vous joueriez', 'ils joueraient'],
        'passé simple': ['je jouai', 'tu jouas', 'il joua', 'nous jouâmes', 'vous jouâtes', 'ils jouèrent'],
        'plus que parfait': ['j\' avais joué', 'tu avais joué', 'il avait joué', 'nous avions joué', 'vous aviez joué', 'ils avaient joué'],
        'subjonctif présent': ['que je joue', 'que tu joues', 'qu\' il joue', 'que nous jouions', 'que vous jouiez', 'qu\' ils jouent'],
        'conditionnel passé': ['j\' aurais joué', 'tu aurais joué', 'il aurait joué', 'nous aurions joué', 'vous auriez joué', 'ils auraient joué'],
        'futur antérieur': ['j\' aurai joué', 'tu auras joué', 'il aura joué', 'nous aurons joué', 'vous aurez joué', 'ils auront joué'],
    },

    # Verbes du deuxième groupe
    'finir': {
        'présent': ['je finis', 'tu finis', 'il finit', 'nous finissons', 'vous finissez', 'ils finissent'],
        'passé composé': ['j\' ai fini', 'tu as fini', 'il a fini', 'nous avons fini', 'vous avez fini', 'ils ont fini'],
        'imparfait': ['je finissais', 'tu finissais', 'il finissait', 'nous finissions', 'vous finissiez', 'ils finissaient'],
        'futur simple': ['je finirai', 'tu finiras', 'il finira', 'nous finirons', 'vous finirez', 'ils finiront'],
        'conditionnel présent': ['je finirais', 'tu finirais', 'il finirait', 'nous finirions', 'vous finiriez', 'ils finiraient'],
        'passé simple': ['je finis', 'tu finis', 'il finit', 'nous finîmes', 'vous finîtes', 'ils finirent'],
        'plus que parfait': ['j\' avais fini', 'tu avais fini', 'il avait fini', 'nous avions fini', 'vous aviez fini', 'ils avaient fini'],
        'subjonctif présent': ['que je finisse', 'que tu finisses', 'qu\' il finisse', 'que nous finissions', 'que vous finissiez', 'qu\' ils finissent'],
        'conditionnel passé': ['j\' aurais fini', 'tu aurais fini', 'il aurait fini', 'nous aurions fini', 'vous auriez fini', 'ils auraient fini'],
        'futur antérieur': ['j\' aurai fini', 'tu auras fini', 'il aura fini', 'nous aurons fini', 'vous aurez fini', 'ils auront fini'],
    },
    'choisir': {
        'présent': ['je choisis', 'tu choisis', 'il choisit', 'nous choisissons', 'vous choisissez', 'ils choisissent'],
        'passé composé': ['j\' ai choisi', 'tu as choisi', 'il a choisi', 'nous avons choisi', 'vous avez choisi', 'ils ont choisi'],
        'imparfait': ['je choisissais', 'tu choisissais', 'il choisissait', 'nous choisissions', 'vous choisissiez', 'ils choisissaient'],
        'futur simple': ['je choisirai', 'tu choisiras', 'il choisira', 'nous choisirons', 'vous choisirez', 'ils choisiront'],
        'conditionnel présent': ['je choisirais', 'tu choisirais', 'il choisirait', 'nous choisirions', 'vous choisiriez', 'ils choisiraient'],
        'passé simple': ['je choisis', 'tu choisis', 'il choisit', 'nous choisîmes', 'vous choisîtes', 'ils choisirent'],
        'plus que parfait': ['j\' avais choisi', 'tu avais choisi', 'il avait choisi', 'nous avions choisi', 'vous aviez choisi', 'ils avaient choisi'],
        'subjonctif présent': ['que je choisisse', 'que tu choisisses', 'qu\' il choisisse', 'que nous choisissions', 'que vous choisissiez', 'qu\' ils choisissent'],
        'conditionnel passé': ['j\' aurais choisi', 'tu aurais choisi', 'il aurait choisi', 'nous aurions choisi', 'vous auriez choisi', 'ils auraient choisi'],
        'futur antérieur': ['j\' aurai choisi', 'tu auras choisi', 'il aura choisi', 'nous aurons choisi', 'vous aurez choisi', 'ils auront choisi']
    },
    'grandir': {
        'présent': ['je grandis', 'tu grandis', 'il grandit', 'nous grandissons', 'vous grandissez', 'ils grandissent'],
        'passé composé': ['j\' ai grandi', 'tu as grandi', 'il a grandi', 'nous avons grandi', 'vous avez grandi', 'ils ont grandi'],
        'imparfait': ['je grandissais', 'tu grandissais', 'il grandissait', 'nous grandissions', 'vous grandissiez', 'ils grandissaient'],
        'futur simple': ['je grandirai', 'tu grandiras', 'il grandira', 'nous grandirons', 'vous grandirez', 'ils grandiront'],
        'conditionnel présent': ['je grandirais', 'tu grandirais', 'il grandirait', 'nous grandirions', 'vous grandiriez', 'ils grandiraient'],
        'passé simple': ['je grandis', 'tu grandis', 'il grandit', 'nous grandîmes', 'vous grandîtes', 'ils grandirent'],
        'plus que parfait': ['j\' avais grandi', 'tu avais grandi', 'il avait grandi', 'nous avions grandi', 'vous aviez grandi', 'ils avaient grandi'],
        'subjonctif présent': ['que je grandisse', 'que tu grandisses', 'qu\' il grandisse', 'que nous grandissions', 'que vous grandissiez', 'qu\' ils grandissent'],
        'conditionnel passé': ['j\' aurais grandi', 'tu aurais grandi', 'il aurait grandi', 'nous aurions grandi', 'vous auriez grandi', 'ils auraient grandi'],
        'futur antérieur': ['j\' aurai grandi', 'tu auras grandi', 'il aura grandi', 'nous aurons grandi', 'vous aurez grandi', 'ils auront grandi'],
    },
    'réussir': {
        'présent': ['je réussis', 'tu réussis', 'il réussit', 'nous réussissons', 'vous réussissez', 'ils réussissent'],
        'passé composé': ['j\' ai réussi', 'tu as réussi', 'il a réussi', 'nous avons réussi', 'vous avez réussi', 'ils ont réussi'],
        'imparfait': ['je réussissais', 'tu réussissais', 'il réussissait', 'nous réussissions', 'vous réussissiez', 'ils réussissaient'],
        'futur simple': ['je réussirai', 'tu réussiras', 'il réussira', 'nous réussirons', 'vous réussirez', 'ils réussiront'],
        'passé simple': ['je réussis', 'tu réussis', 'il réussit', 'nous réussîmes', 'vous réussîtes', 'ils réussirent'],
        'plus que parfait': ['j\' avais réussi', 'tu avais réussi', 'il avait réussi', 'nous avions réussi', 'vous aviez réussi', 'ils avaient réussi'],
        'subjonctif présent': ['que je réussisse', 'que tu réussisses', 'qu\' il réussisse', 'que nous réussissions', 'que vous réussissiez', 'qu\' ils réussissent'],
        'conditionnel passé': ['j\' aurais réussi', 'tu aurais réussi', 'il aurait réussi', 'nous aurions réussi', 'vous auriez réussi', 'ils auraient réussi'],
        'futur antérieur': ['j\' aurai réussi', 'tu auras réussi', 'il aura réussi', 'nous aurons réussi', 'vous aurez réussi', 'ils auront réussi']
    },
    'remplir': {
        'présent': ['je remplis', 'tu remplis', 'il remplit', 'nous remplissons', 'vous remplissez', 'ils remplissent'],
        'passé composé': ['j\' ai rempli', 'tu as rempli', 'il a rempli', 'nous avons rempli', 'vous avez rempli', 'ils ont rempli'],
        'imparfait': ['je remplissais', 'tu remplissais', 'il remplissait', 'nous remplissions', 'vous remplissiez', 'ils remplissaient'],
        'futur simple': ['je remplirai', 'tu rempliras', 'il remplira', 'nous remplirons', 'vous remplirez', 'ils rempliront'],
        'conditionnel présent': ['je remplirais', 'tu remplirais', 'il remplirait', 'nous remplirions', 'vous rempliriez', 'ils rempliraient'],
        'passé simple': ['je remplis', 'tu remplis', 'il remplit', 'nous remplîmes', 'vous remplîtes', 'ils remplirent'],
        'plus que parfait': ['j\' avais rempli', 'tu avais rempli', 'il avait rempli', 'nous avions rempli', 'vous aviez rempli', 'ils avaient rempli'],
        'subjonctif présent': ['que je remplisse', 'que tu remplisses', 'qu\' il remplisse', 'que nous remplissions', 'que vous remplissiez', 'qu\' ils remplissent'],
        'conditionnel passé': ['j\' aurais rempli', 'tu aurais rempli', 'il aurait rempli', 'nous aurions rempli', 'vous auriez rempli', 'ils auraient rempli'],
        'futur antérieur': ['j\' aurai rempli', 'tu auras rempli', 'il aura rempli', 'nous aurons rempli', 'vous aurez rempli', 'ils auront rempli']
    },

    # Verbes du troisième groupe
    'être': {
        'présent': ['je suis', 'tu es', 'il est', 'nous sommes', 'vous êtes', 'ils sont'],
        'passé composé': ['j\' ai été', 'tu as été', 'il a été', 'nous avons été', 'vous avez été', 'ils ont été'],
        'imparfait': ['j\' étais', 'tu étais', 'il était', 'nous étions', 'vous étiez', 'ils étaient'],
        'futur simple': ['je serai', 'tu seras', 'il sera', 'nous serons', 'vous serez', 'ils seront'],
        'conditionnel présent': ['je serais', 'tu serais', 'il serait', 'nous serions', 'vous seriez', 'ils seraient'],
        'passé simple': ['je fus', 'tu fus', 'il fut', 'nous fûmes', 'vous fûtes', 'ils furent'],
        'plus que parfait': ['j\' avais été', 'tu avais été', 'il avait été', 'nous avions été', 'vous aviez été', 'ils avaient été'],
        'subjonctif présent': ['que je sois', 'que tu sois', 'qu\' il soit', 'que nous soyons', 'que vous soyez', 'qu\' ils soient'],
        'conditionnel passé': ['j\' aurais été', 'tu aurais été', 'il aurait été', 'nous aurions été', 'vous auriez été', 'ils auraient été'],
        'futur antérieur': ['j\' aurai été', 'tu auras été', 'il aura été', 'nous aurons été', 'vous aurez été', 'ils auront été'],
    },
    'avoir': {
        'présent': ['j\' ai', 'tu as', 'il a', 'nous avons', 'vous avez', 'ils ont'],
        'passé composé': ['j\' ai eu', 'tu as eu', 'il a eu', 'nous avons eu', 'vous avez eu', 'ils ont eu'],
        'imparfait': ['j\' avais', 'tu avais', 'il avait', 'nous avions', 'vous aviez', 'ils avaient'],
        'futur simple': ['j\' aurai', 'tu auras', 'il aura', 'nous aurons', 'vous aurez', 'ils auront'],
        'conditionnel présent': ['j\' aurais', 'tu aurais', 'il aurait', 'nous aurions', 'vous auriez', 'ils auraient'],
        'passé simple': ['j\' eus', 'tu eus', 'il eut', 'nous eûmes', 'vous eûtes', 'ils eurent'],
        'plus que parfait': ['j\' avais eu', 'tu avais eu', 'il avait eu', 'nous avions eu', 'vous aviez eu', 'ils avaient eu'],
        'subjonctif présent': ['que j\' aie', 'que tu aies', 'qu\' il ait', 'que nous ayons', 'que vous ayez', 'qu\' ils aient'],
        'conditionnel passé': ['j\' aurais eu', 'tu aurais eu', 'il aurait eu', 'nous aurions eu', 'vous auriez eu', 'ils auraient eu'],
        'futur antérieur': ['j\' aurai eu', 'tu auras eu', 'il aura eu', 'nous aurons eu', 'vous aurez eu', 'ils auront eu']
    },
    'faire': {
        'présent': ['je fais', 'tu fais', 'il fait', 'nous faisons', 'vous faites', 'ils font'],
        'passé composé': ['j\' ai fait', 'tu as fait', 'il a fait', 'nous avons fait', 'vous avez fait', 'ils ont fait'],
        'imparfait': ['je faisais', 'tu faisais', 'il faisait', 'nous faisions', 'vous faisiez', 'ils faisaient'],
        'futur simple': ['je ferai', 'tu feras', 'il fera', 'nous ferons', 'vous ferez', 'ils feront'],
        'conditionnel présent': ['je ferais', 'tu ferais', 'il ferait', 'nous ferions', 'vous feriez', 'ils feraient'],
        'passé simple': ['je fis', 'tu fis', 'il fit', 'nous fîmes', 'vous fîtes', 'ils firent'],
        'plus-que-parfait': ['j\' avais fait', 'tu avais fait', 'il avait fait', 'nous avions fait', 'vous aviez fait', 'ils avaient fait'],
        'subjonctif présent': ['que je fasse', 'que tu fasses', 'qu\' il fasse', 'que nous fassions', 'que vous fassiez', 'qu\' ils fassent'],
        'conditionnel passé': ['j\' aurais fait', 'tu aurais fait', 'il aurait fait', 'nous aurions fait', 'vous auriez fait', 'ils auraient fait'],
        'futur antérieur': ['j\' aurai fait', 'tu auras fait', 'il aura fait', 'nous aurons fait', 'vous aurez fait', 'ils auront fait']
    },
    'dire': {
        'présent': ['je dis', 'tu dis', 'il dit', 'nous disons', 'vous dites', 'ils disent'],
        'passé composé': ['j\' ai dit', 'tu as dit', 'il a dit', 'nous avons dit', 'vous avez dit', 'ils ont dit'],
        'imparfait': ['je disais', 'tu disais', 'il disait', 'nous disions', 'vous disiez', 'ils disaient'],
        'futur simple': ['je dirai', 'tu diras', 'il dira', 'nous dirons', 'vous direz', 'ils diront'],
        'conditionnel présent': ['je dirais', 'tu dirais', 'il dirait', 'nous dirions', 'vous diriez', 'ils diraient'],
        'passé simple': ['je dis', 'tu dis', 'il dit', 'nous dîmes', 'vous dîtes', 'ils dirent'],
        'plus-que-parfait': ['j\' avais dit', 'tu avais dit', 'il avait dit', 'nous avions dit', 'vous aviez dit', 'ils avaient dit'],
        'subjonctif présent': ['que je dise', 'que tu dises', 'qu\' il dise', 'que nous disions', 'que vous disiez', 'qu\' ils disent'],
        'conditionnel passé': ['j\' aurais dit', 'tu aurais dit', 'il aurait dit', 'nous aurions dit', 'vous auriez dit', 'ils auraient dit'],
        'futur antérieur': ['j\' aurai dit', 'tu auras dit', 'il aura dit', 'nous aurons dit', 'vous aurez dit', 'ils auront dit']
    },
    'aller': {
        'présent': ['je vais', 'tu vas', 'il va', 'nous allons', 'vous allez', 'ils vont'],
        'passé composé': ['je suis allé', 'tu es allé', 'il est allé', 'nous sommes allés', 'vous êtes allés', 'ils sont allés'],
        'imparfait': ['j\' allais', 'tu allais', 'il allait', 'nous allions', 'vous alliez', 'ils allaient'],
        'futur simple': ['j\' irai', 'tu iras', 'il ira', 'nous irons', 'vous irez', 'ils iront'],
        'conditionnel présent': ['j\' irais', 'tu irais', 'il irait', 'nous irions', 'vous iriez', 'ils iraient'],
        'passé simple': ['j\' allai', 'tu allas', 'il alla', 'nous allâmes', 'vous allâtes', 'ils allèrent'],
        'plus-que-parfait': ['j\' étais allé', 'tu étais allé', 'il était allé', 'nous étions allés', 'vous étiez allés', 'ils étaient allés'],
        'subjonctif présent': ['que j\' aille', 'que tu ailles', 'qu\' il aille', 'que nous allions', 'que vous alliez', 'qu\' ils aillent'],
        'conditionnel passé': ['je serais allé', 'tu serais allé', 'il serait allé', 'nous serions allés', 'vous seriez allés', 'ils seraient allés'],
        'futur antérieur': ['je serai allé', 'tu seras allé', 'il sera allé', 'nous serons allés', 'vous serez allés', 'ils seront allés']
    },
    'voir': {
        'présent': ['je vois', 'tu vois', 'il voit', 'nous voyons', 'vous voyez', 'ils voient'],
        'passé composé': ['j\' ai vu', 'tu as vu', 'il a vu', 'nous avons vu', 'vous avez vu', 'ils ont vu'],
        'imparfait': ['je voyais', 'tu voyais', 'il voyait', 'nous voyions', 'vous voyiez', 'ils voyaient'],
        'futur simple': ['je verrai', 'tu verras', 'il verra', 'nous verrons', 'vous verrez', 'ils verront'],
        'conditionnel présent': ['je verrais', 'tu verrais', 'il verrait', 'nous verrions', 'vous verriez', 'ils verraient'],
        'passé simple': ['je vis', 'tu vis', 'il vit', 'nous vîmes', 'vous vîtes', 'ils virent'],
        'plus-que-parfait': ['j\' avais vu', 'tu avais vu', 'il avait vu', 'nous avions vu', 'vous aviez vu', 'ils avaient vu'],
        'subjonctif présent': ['que je voie', 'que tu voies', 'qu\' il voie', 'que nous voyions', 'que vous voyiez', 'qu\' ils voient'],
        'conditionnel passé': ['j\' aurais vu', 'tu aurais vu', 'il aurait vu', 'nous aurions vu', 'vous auriez vu', 'ils auraient vu'],
        'futur antérieur': ['j\' aurai vu', 'tu auras vu', 'il aura vu', 'nous aurons vu', 'vous aurez vu', 'ils auront vu']
    },
    "savoir": {
        "présent": ["je sais", "tu sais", "il sait", "nous savons", "vous savez", "ils savent"],
        "passé composé": ["j\' ai su", "tu as su", "il a su", "nous avons su", "vous avez su", "ils ont su"],
        "imparfait": ["je savais", "tu savais", "il savait", "nous savions", "vous saviez", "ils savaient"],
        "futur simple": ["je saurai", "tu sauras", "il saura", "nous saurons", "vous saurez", "ils sauront"],
        "conditionnel présent": ["je saurais", "tu saurais", "il saurait", "nous saurions", "vous sauriez", "ils sauraient"],
        "passé simple": ["je sus", "tu sus", "il sut", "nous sûmes", "vous sûtes", "ils surent"],
        "plus-que-parfait": ["j\' avais su", "tu avais su", "il avait su", "nous avions su", "vous aviez su", "ils avaient su"],
        "subjonctif présent": ["que je sache", "que tu saches", "qu\' il sache", "que nous sachions", "que vous sachiez", "qu\' ils sachent"],
        "conditionnel passé": ["j\' aurais su", "tu aurais su", "il aurait su", "nous aurions su", "vous auriez su", "ils auraient su"],
        "futur antérieur": ["j\' aurai su", "tu auras su", "il aura su", "nous aurons su", "vous aurez su", "ils auront su"]
    },
    "pouvoir": {
        "présent": ["je peux", "tu peux", "il peut", "nous pouvons", "vous pouvez", "ils peuvent"],
        "passé composé": ["j\' ai pu", "tu as pu", "il a pu", "nous avons pu", "vous avez pu", "ils ont pu"],
        "imparfait": ["je pouvais", "tu pouvais", "il pouvait", "nous pouvions", "vous pouviez", "ils pouvaient"],
        "futur simple": ["je pourrai", "tu pourras", "il pourra", "nous pourrons", "vous pourrez", "ils pourront"],
        "conditionnel présent": ["je pourrais", "tu pourrais", "il pourrait", "nous pourrions", "vous pourriez", "ils pourraient"],
        "passé simple": ["je pus", "tu pus", "il put", "nous pûmes", "vous pûtes", "ils purent"],
        "plus-que-parfait": ["j\' avais pu", "tu avais pu", "il avait pu", "nous avions pu", "vous aviez pu", "ils avaient pu"],
        "subjonctif présent": ["que je puisse", "que tu puisses", "qu\' il puisse", "que nous puissions", "que vous puissiez", "qu\' ils puissent"],
        "conditionnel passé": ["j\' aurais pu", "tu aurais pu", "il aurait pu", "nous aurions pu", "vous auriez pu", "ils auraient pu"],
        "futur antérieur": ["j\' aurai pu", "tu auras pu", "il aura pu", "nous aurons pu", "vous aurez pu", "ils auront pu"]
    },
    "vouloir": {
        "présent": ["je veux", "tu veux", "il veut", "nous voulons", "vous voulez", "ils veulent"],
        "passé composé": ["j\' ai voulu", "tu as voulu", "il a voulu", "nous avons voulu", "vous avez voulu", "ils ont voulu"],
        "imparfait": ["je voulais", "tu voulais", "il voulait", "nous voulions", "vous vouliez", "ils voulaient"],
        "futur simple": ["je voudrai", "tu voudras", "il voudra", "nous voudrons", "vous voudrez", "ils voudront"],
        "conditionnel présent": ["je voudrais", "tu voudrais", "il voudrait", "nous voudrions", "vous voudriez", "ils voudraient"],
        "passé simple": ["je voulus", "tu voulus", "il voulut", "nous voulûmes", "vous voulûtes", "ils voulurent"],
        "plus-que-parfait": ["j\' avais voulu", "tu avais voulu", "il avait voulu", "nous avions voulu", "vous aviez voulu", "ils avaient voulu"],
        "subjonctif présent": ["que je veuille", "que tu veuilles", "qu\' il veuille", "que nous voulions", "que vous vouliez", "qu\' ils veuillent"],
        "conditionnel passé": ["j\' aurais voulu", "tu aurais voulu", "il aurait voulu", "nous aurions voulu", "vous auriez voulu", "ils auraient voulu"],
        "futur antérieur": ["j\' aurai voulu", "tu auras voulu", "il aura voulu", "nous aurons voulu", "vous aurez voulu", "ils auront voulu"]
    },
    "venir": {
        "présent": ["je viens", "tu viens", "il vient", "nous venons", "vous venez", "ils viennent"],
        "passé composé": ["je suis venu", "tu es venu", "il est venu", "nous sommes venus", "vous êtes venus", "ils sont venus"],
        "imparfait": ["je venais", "tu venais", "il venait", "nous venions", "vous veniez", "ils venaient"],
        "futur simple": ["je viendrai", "tu viendras", "il viendra", "nous viendrons", "vous viendrez", "ils viendront"],
        "conditionnel présent": ["je viendrais", "tu viendrais", "il viendrait", "nous viendrions", "vous viendriez", "ils viendraient"],
        "passé simple": ["je vins", "tu vins", "il vint", "nous vînmes", "vous vîntes", "ils vinrent"],
        "plus-que-parfait": ["j\' étais venu", "tu étais venu", "il était venu", "nous étions venus", "vous étiez venus", "ils étaient venus"],
        "subjonctif présent": ["que je vienne", "que tu viennes", "qu\' il vienne", "que nous venions", "que vous veniez", "qu\' ils viennent"],
        "conditionnel passé": ["je serais venu", "tu serais venu", "il serait venu", "nous serions venus", "vous seriez venus", "ils seraient venus"],
        "futur antérieur": ["je serai venu", "tu seras venu", "il sera venu", "nous serons venus", "vous serez venus", "ils seront venus"]
    },
    "prendre": {
        "présent": ["je prends", "tu prends", "il prend", "nous prenons", "vous prenez", "ils prennent"],
        "passé composé": ["j\' ai pris", "tu as pris", "il a pris", "nous avons pris", "vous avez pris", "ils ont pris"],
        "imparfait": ["je prenais", "tu prenais", "il prenait", "nous prenions", "vous preniez", "ils prenaient"],
        "futur simple": ["je prendrai", "tu prendras", "il prendra", "nous prendrons", "vous prendrez", "ils prendront"],
        "conditionnel présent": ["je prendrais", "tu prendrais", "il prendrait", "nous prendrions", "vous prendriez", "ils prendraient"],
        "passé simple": ["je pris", "tu pris", "il prit", "nous prîmes", "vous prîtes", "ils prirent"],
        "plus-que-parfait": ["j\' avais pris", "tu avais pris", "il avait pris", "nous avions pris", "vous aviez pris", "ils avaient pris"],
        "subjonctif présent": ["que je prenne", "que tu prennes", "qu\' il prenne", "que nous prenions", "que vous preniez", "qu\' ils prennent"],
        "conditionnel passé": ["j\' aurais pris", "tu aurais pris", "il aurait pris", "nous aurions pris", "vous auriez pris", "ils auraient pris"],
        "futur antérieur": ["j\' aurai pris", "tu auras pris", "il aura pris", "nous aurons pris", "vous aurez pris", "ils auront pris"]
    },
    "devoir": {
        "présent": ["je dois", "tu dois", "il doit", "nous devons", "vous devez", "ils doivent"],
        "passé composé": ["j\' ai dû", "tu as dû", "il a dû", "nous avons dû", "vous avez dû", "ils ont dû"],
        "imparfait": ["je devais", "tu devais", "il devait", "nous devions", "vous deviez", "ils devaient"],
        "futur simple": ["je devrai", "tu devras", "il devra", "nous devrons", "vous devrez", "ils devront"],
        "conditionnel présent": ["je devrais", "tu devrais", "il devrait", "nous devrions", "vous devriez", "ils devraient"],
        "passé simple": ["je dus", "tu dus", "il dut", "nous dûmes", "vous dûtes", "ils durent"],
        "plus-que-parfait": ["j\' avais dû", "tu avais dû", "il avait dû", "nous avions dû", "vous aviez dû", "ils avaient dû"],
        "subjonctif présent": ["que je doive", "que tu doives", "qu\' il doive", "que nous devions", "que vous deviez", "qu\' ils doivent"],
        "conditionnel passé": ["j\' aurais dû", "tu aurais dû", "il aurait dû", "nous aurions dû", "vous auriez dû", "ils auraient dû"],
        "futur antérieur": ["j\' aurai dû", "tu auras dû", "il aura dû", "nous aurons dû", "vous aurez dû", "ils auront dû"]
    },
    "mettre": {
        "présent": ["je mets", "tu mets", "il met", "nous mettons", "vous mettez", "ils mettent"],
        "passé composé": ["j\' ai mis", "tu as mis", "il a mis", "nous avons mis", "vous avez mis", "ils ont mis"],
        "imparfait": ["je mettais", "tu mettais", "il mettait", "nous mettions", "vous mettiez", "ils mettaient"],
        "futur simple": ["je mettrai", "tu mettras", "il mettra", "nous mettrons", "vous mettrez", "ils mettront"],
        "conditionnel présent": ["je mettrais", "tu mettrais", "il mettrait", "nous mettrions", "vous mettriez", "ils mettraient"],
        "passé simple": ["je mis", "tu mis", "il mit", "nous mîmes", "vous mîtes", "ils mirent"],
        "plus-que-parfait": ["j\' avais mis", "tu avais mis", "il avait mis", "nous avions mis", "vous aviez mis", "ils avaient mis"],
        "subjonctif présent": ["que je mette", "que tu mettes", "qu\' il mette", "que nous mettions", "que vous mettiez", "qu\' ils mettent"],
        "conditionnel passé": ["j\' aurais mis", "tu aurais mis", "il aurait mis", "nous aurions mis", "vous auriez mis", "ils auraient mis"],
        "futur antérieur": ["j\' aurai mis", "tu auras mis", "il aura mis", "nous aurons mis", "vous aurez mis", "ils auront mis"]
    },
    "lire": {
        "présent": ["je lis", "tu lis", "il lit", "nous lisons", "vous lisez", "ils lisent"],
        "passé composé": ["j\' ai lu", "tu as lu", "il a lu", "nous avons lu", "vous avez lu", "ils ont lu"],
        "imparfait": ["je lisais", "tu lisais", "il lisait", "nous lisions", "vous lisiez", "ils lisaient"],
        "futur simple": ["je lirai", "tu liras", "il lira", "nous lirons", "vous lirez", "ils liront"],
        "conditionnel présent": ["je lirais", "tu lirais", "il lirait", "nous lirions", "vous liriez", "ils liraient"],
        "passé simple": ["je lus", "tu lus", "il lut", "nous lûmes", "vous lûtes", "ils lurent"],
        "plus-que-parfait": ["j\' avais lu", "tu avais lu", "il avait lu", "nous avions lu", "vous aviez lu", "ils avaient lu"],
        "subjonctif présent": ["que je lise", "que tu lises", "qu\' il lise", "que nous lisions", "que vous lisiez", "qu\' ils lisent"],
        "conditionnel passé": ["j\' aurais lu", "tu aurais lu", "il aurait lu", "nous aurions lu", "vous auriez lu", "ils auraient lu"],
        "futur antérieur": ["j\' aurai lu", "tu auras lu", "il aura lu", "nous aurons lu", "vous aurez lu", "ils auront lu"]
    },
    "écrire": {
        "présent": ["j\' écris", "tu écris", "il écrit", "nous écrivons", "vous écrivez", "ils écrivent"],
        "passé composé": ["j\' ai écrit", "tu as écrit", "il a écrit", "nous avons écrit", "vous avez écrit", "ils ont écrit"],
        "imparfait": ["j\' écrivais", "tu écrivais", "il écrivait", "nous écrivions", "vous écriviez", "ils écrivaient"],
        "futur simple": ["j\' écrirai", "tu écriras", "il écrira", "nous écrirons", "vous écrirez", "ils écriront"],
        "conditionnel présent": ["j\' écrirais", "tu écrirais", "il écrirait", "nous écririons", "vous écririez", "ils écriraient"],
        "passé simple": ["j\' écrivis", "tu écrivis", "il écrivit", "nous écrivîmes", "vous écrivîtes", "ils écrivirent"],
        "plus-que-parfait": ["j\' avais écrit", "tu avais écrit", "il avait écrit", "nous avions écrit", "vous aviez écrit", "ils avaient écrit"],
        "subjonctif présent": ["que j\' écrive", "que tu écrives", "qu\' il écrive", "que nous écrivions", "que vous écriviez", "qu\' ils écrivent"],
        "conditionnel passé": ["j\' aurais écrit", "tu aurais écrit", "il aurait écrit", "nous aurions écrit", "vous auriez écrit", "ils auraient écrit"],
        "futur antérieur": ["j\' aurai écrit", "tu auras écrit", "il aura écrit", "nous aurons écrit", "vous aurez écrit", "ils auront écrit"]
    },
    "dire": {
        "présent": ["je dis", "tu dis", "il dit", "nous disons", "vous dites", "ils disent"],
        "passé composé": ["j\' ai dit", "tu as dit", "il a dit", "nous avons dit", "vous avez dit", "ils ont dit"],
        "imparfait": ["je disais", "tu disais", "il disait", "nous disions", "vous disiez", "ils disaient"],
        "futur simple": ["je dirai", "tu diras", "il dira", "nous dirons", "vous direz", "ils diront"],
        "conditionnel présent": ["je dirais", "tu dirais", "il dirait", "nous dirions", "vous diriez", "ils diraient"],
        "passé simple": ["je dis", "tu dis", "il dit", "nous dîmes", "vous dîtes", "ils dirent"],
        "plus-que-parfait": ["j\' avais dit", "tu avais dit", "il avait dit", "nous avions dit", "vous aviez dit", "ils avaient dit"],
        "subjonctif présent": ["que je dise", "que tu dises", "qu\' il dise", "que nous disions", "que vous disiez", "qu\' ils disent"],
        "conditionnel passé": ["j\' aurais dit", "tu aurais dit", "il aurait dit", "nous aurions dit", "vous auriez dit", "ils auraient dit"],
        "futur antérieur": ["j\' aurai dit", "tu auras dit", "il aura dit", "nous aurons dit", "vous aurez dit", "ils auront dit"]
    },

    "partir": {
        "présent": ["je pars", "tu pars", "il part", "nous partons", "vous partez", "ils partent"],
        "passé composé": ["je suis parti", "tu es parti", "il est parti", "nous sommes partis", "vous êtes partis", "ils sont partis"],
        "imparfait": ["je partais", "tu partais", "il partait", "nous partions", "vous partiez", "ils partaient"],
        "futur simple": ["je partirai", "tu partiras", "il partira", "nous partirons", "vous partirez", "ils partiront"],
        "conditionnel présent": ["je partirais", "tu partirais", "il partirait", "nous partirions", "vous partiriez", "ils partiraient"],
        "passé simple": ["je partis", "tu partis", "il partit", "nous partîmes", "vous partîtes", "ils partirent"],
        "plus-que-parfait": ["j\' étais parti", "tu étais parti", "il était parti", "nous étions partis", "vous étiez partis", "ils étaient partis"],
        "subjonctif présent": ["que je parte", "que tu partes", "qu\' il parte", "que nous partions", "que vous partiez", "qu\' ils partent"],
        "conditionnel passé": ["je serais parti", "tu serais parti", "il serait parti", "nous serions partis", "vous seriez partis", "ils seraient partis"],
        "futur antérieur": ["je serai parti", "tu seras parti", "il sera parti", "nous serons partis", "vous serez partis", "ils seront partis"]
    },
    "courir": {
        "présent": ["je cours", "tu cours", "il court", "nous courons", "vous courez", "ils courent"],
        "passé composé": ["j\' ai couru", "tu as couru", "il a couru", "nous avons couru", "vous avez couru", "ils ont couru"],
        "imparfait": ["je courais", "tu courais", "il courait", "nous courions", "vous couriez", "ils couraient"],
        "futur simple": ["je courrai", "tu courras", "il courra", "nous courrons", "vous courrez", "ils courront"],
        "conditionnel présent": ["je courrais", "tu courrais", "il courrait", "nous courrions", "vous courriez", "ils courraient"],
        "passé simple": ["je courus", "tu courus", "il courut", "nous courûmes", "vous courûtes", "ils coururent"],
        "plus-que-parfait": ["j\' étais sorti", "tu étais sorti", "il était sorti", "nous étions sortis", "vous étiez sortis", "ils étaient sortis"],
        "subjonctif présent": ["que je sorte", "que tu sortes", "qu\' il sorte", "que nous sortions", "que vous sortiez", "qu\' ils sortent"],
        "conditionnel passé": ["je serais sorti", "tu serais sorti", "il serait sorti", "nous serions sortis", "vous seriez sortis", "ils seraient sortis"],
        "futur antérieur": ["je serai sorti", "tu seras sorti", "il sera sorti", "nous serons sortis", "vous serez sortis", "ils seront sortis"]
    },
    "mourir": {
        "présent": ["je meurs", "tu meurs", "il meurt", "nous mourons", "vous mourez", "ils meurent"],
        "passé composé": ["je suis mort", "tu es mort", "il est mort", "nous sommes morts", "vous êtes morts", "ils sont morts"],
        "imparfait": ["je mourais", "tu mourais", "il mourait", "nous mourions", "vous mouriez", "ils mouraient"],
        "futur simple": ["je mourrai", "tu mourras", "il mourra", "nous mourrons", "vous mourrez", "ils mourront"],
        "conditionnel présent": ["je mourrais", "tu mourrais", "il mourrait", "nous mourrions", "vous mourriez", "ils mourraient"],
        "passé simple": ["je mourus", "tu mourus", "il mourut", "nous mourûmes", "vous mourûtes", "ils moururent"],
        "plus-que-parfait": ["j'étais mort", "tu étais mort", "il était mort", "nous étions morts", "vous étiez morts", "ils étaient morts"],
        "subjonctif présent": ["que je meure", "que tu meures", "qu' il meure", "que nous mourions", "que vous mouriez", "qu' ils meurent"],
        "conditionnel passé": ["je serais mort", "tu serais mort", "il serait mort", "nous serions morts", "vous seriez morts", "ils seraient morts"],
        "futur antérieur": ["je serai mort", "tu seras mort", "il sera mort", "nous serons morts", "vous serez morts", "ils seront morts"]
    },
    'fuir': {
        'présent': ['je fuis', 'tu fuis', 'il fuit', 'nous fuyons', 'vous fuyez', 'ils fuient'],
        'passé composé': ['j\' ai fui', 'tu as fui', 'il a fui', 'nous avons fui', 'vous avez fui', 'ils ont fui'],
        'imparfait': ['je fuyais', 'tu fuyais', 'il fuyait', 'nous fuyions', 'vous fuyiez', 'ils fuyaient'],
        'futur simple': ['je fuirai', 'tu fuiras', 'il fuira', 'nous fuirons', 'vous fuirez', 'ils fuiront'],
        'conditionnel présent': ['je fuirais', 'tu fuirais', 'il fuirait', 'nous fuirions', 'vous fuiriez', 'ils fuiraient'],
        'passé simple': ['je fuis', 'tu fuis', 'il fuit', 'nous fuîmes', 'vous fuîtes', 'ils fuirent'],
        "plus-que-parfait": ["j'avais fui", "tu avais fui", "il avait fui", "nous avions fui", "vous aviez fui", "ils avaient fui"],
        "subjonctif présent": ["que je fuie", "que tu fuies", "qu' il fuie", "que nous fuyions", "que vous fuyiez", "qu' ils fuient"],
        "conditionnel passé": ["j'aurais fui", "tu aurais fui", "il aurait fui", "nous aurions fui", "vous auriez fui", "ils auraient fui"],
        "futur antérieur": ["j'aurai fui", "tu auras fui", "il aura fui", "nous aurons fui", "vous aurez fui", "ils auront fui"]
    },
    'tenir': {
        'présent': ['je tiens', 'tu tiens', 'il tient', 'nous tenons', 'vous tenez', 'ils tiennent'],
        'passé composé': ['j\' ai tenu', 'tu as tenu', 'il a tenu', 'nous avons tenu', 'vous avez tenu', 'ils ont tenu'],
        'imparfait': ['je tenais', 'tu tenais', 'il tenait', 'nous tenions', 'vous teniez', 'ils tenaient'],
        'futur simple': ['je tiendrai', 'tu tiendras', 'il tiendra', 'nous tiendrons', 'vous tiendrez', 'ils tiendront'],
        'conditionnel présent': ['je tiendrais', 'tu tiendrais', 'il tiendrait', 'nous tiendrions', 'vous tiendriez', 'ils tiendraient'],
        'passé simple': ['je tins', 'tu tins', 'il tint', 'nous tînmes', 'vous tîntes', 'ils tinrent'],
        "plus-que-parfait": ["j'avais tenu", "tu avais tenu", "il avait tenu", "nous avions tenu", "vous aviez tenu", "ils avaient tenu"],
        "subjonctif présent": ["que je tienne", "que tu tiennes", "qu' il tienne", "que nous tenions", "que vous teniez", "qu' ils tiennent"],
        "conditionnel passé": ["j'aurais tenu", "tu aurais tenu", "il aurait tenu", "nous aurions tenu", "vous auriez tenu", "ils auraient tenu"],
        "futur antérieur": ["j'aurai tenu", "tu auras tenu", "il aura tenu", "nous aurons tenu", "vous aurez tenu", "ils auront tenu"]
    },
    'vaincre': {
        'présent': ['je vaincs', 'tu vaincs', 'il vainc', 'nous vainquons', 'vous vainquez', 'ils vainquent'],
        'passé composé': ['j\' ai vaincu', 'tu as vaincu', 'il a vaincu', 'nous avons vaincu', 'vous avez vaincu', 'ils ont vaincu'],
        'imparfait': ['je vainquais', 'tu vainquais', 'il vainquait', 'nous vainquions', 'vous vainquiez', 'ils vainquaient'],
        'futur simple': ['je vaincrai', 'tu vaincras', 'il vaincra', 'nous vaincrons', 'vous vaincrez', 'ils vaincront'],
        'conditionnel présent': ['je vaincrais', 'tu vaincrais', 'il vaincrait', 'nous vaincrions', 'vous vaincriez', 'ils vaincraient'],
        'passé simple': ['je vainquis', 'tu vainquis', 'il vainquit', 'nous vainquîmes', 'vous vainquîtes', 'ils vainquirent'],
        "plus-que-parfait": ["j'avais vaincu", "tu avais vaincu", "il avait vaincu", "nous avions vaincu", "vous aviez vaincu", "ils avaient vaincu"],
        "subjonctif présent": ["que je vainque", "que tu vainques", "qu' il vainque", "que nous vainquions", "que vous vainquiez", "qu' ils vainquent"],
        "conditionnel passé": ["j'aurais vaincu", "tu aurais vaincu", "il aurait vaincu", "nous aurions vaincu", "vous auriez vaincu", "ils auraient vaincu"],
        "futur antérieur": ["j'aurai vaincu", "tu auras vaincu", "il aura vaincu", "nous aurons vaincu", "vous aurez vaincu", "ils auront vaincu"]
    },
    'vêtir': {
        'présent': ['je vêts', 'tu vêts', 'il vêt', 'nous vêtons', 'vous vêtez', 'ils vêtent'],
        'passé composé': ['j\' ai vêtu', 'tu as vêtu', 'il a vêtu', 'nous avons vêtu', 'vous avez vêtu', 'ils ont vêtu'],
        'imparfait': ['je vêtais', 'tu vêtais', 'il vêtait', 'nous vêtions', 'vous vêtiez', 'ils vêtaient'],
        'futur simple': ['je vêtirai', 'tu vêtiras', 'il vêtira', 'nous vêtirons', 'vous vêtirez', 'ils vêtiront'],
        'conditionnel présent': ['je vêtirais', 'tu vêtirais', 'il vêtirait', 'nous vêtirions', 'vous vêtiriez', 'ils vêtiraient'],
        'passé simple': ['je vêtis', 'tu vêtis', 'il vêtit', 'nous vêtîmes', 'vous vêtîtes', 'ils vêtirent'],
        "plus-que-parfait": ["j'avais vêtu", "tu avais vêtu", "il avait vêtu", "nous avions vêtu", "vous aviez vêtu", "ils avaient vêtu"],
        "subjonctif présent": ["que je vête", "que tu vêtes", "qu' il vête", "que nous vêtions", "que vous vêtiez", "qu' ils vêtent"],
        "conditionnel passé": ["j'aurais vêtu", "tu aurais vêtu", "il aurait vêtu", "nous aurions vêtu", "vous auriez vêtu", "ils auraient vêtu"],
        "futur antérieur": ["j'aurai vêtu", "tu auras vêtu", "il aura vêtu", "nous aurons vêtu", "vous aurez vêtu", "ils auront vêtu"]
    },
    'recevoir': {
        'présent': ['je reçois', 'tu reçois', 'il reçoit', 'nous recevons', 'vous recevez', 'ils reçoivent'],
        'passé composé': ['j\' ai reçu', 'tu as reçu', 'il a reçu', 'nous avons reçu', 'vous avez reçu', 'ils ont reçu'],
        'imparfait': ['je recevais', 'tu recevais', 'il recevait', 'nous recevions', 'vous receviez', 'ils recevaient'],
        'futur simple': ['je recevrai', 'tu recevras', 'il recevra', 'nous recevrons', 'vous recevrez', 'ils recevront'],
        'conditionnel présent': ['je recevrais', 'tu recevrais', 'il recevrait', 'nous recevrions', 'vous recevriez', 'ils recevraient'],
        'passé simple': ['je reçus', 'tu reçus', 'il reçut', 'nous reçûmes', 'vous reçûtes', 'ils reçurent'],
        "plus-que-parfait": ["j'avais reçu", "tu avais reçu", "il avait reçu", "nous avions reçu", "vous aviez reçu", "ils avaient reçu"],
        "subjonctif présent": ["que je reçoive", "que tu reçoives", "qu' il reçoive", "que nous recevions", "que vous receviez", "qu' ils reçoivent"],
        "conditionnel passé": ["j'aurais reçu", "tu aurais reçu", "il aurait reçu", "nous aurions reçu", "vous auriez reçu", "ils auraient reçu"],
        "futur antérieur": ["j'aurai reçu", "tu auras reçu", "il aura reçu", "nous aurons reçu", "vous aurez reçu", "ils auront reçu"]
    },
    'valoir': {
        'présent': ['je vaux', 'tu vaux', 'il vaut', 'nous valons', 'vous valez', 'ils valent'],
        'passé composé': ['j\'ai valu', 'tu as valu', 'il a valu', 'nous avons valu', 'vous avez valu', 'ils ont valu'],
        'imparfait': ['je valais', 'tu valais', 'il valait', 'nous valions', 'vous valiez', 'ils valaient'],
        'futur simple': ['je vaudrai', 'tu vaudras', 'il vaudra', 'nous vaudrons', 'vous vaudrez', 'ils vaudront'],
        'conditionnel présent': ['je vaudrais', 'tu vaudrais', 'il vaudrait', 'nous vaudrions', 'vous vaudriez', 'ils vaudraient'],
        'passé simple': ['je valus', 'tu valus', 'il valut', 'nous valûmes', 'vous valûtes', 'ils valurent'],
        "plus-que-parfait": ["j'avais valu", "tu avais valu", "il avait valu", "nous avions valu", "vous aviez valu", "ils avaient valu"],
        "subjonctif présent": ["que je vaille", "que tu vailles", "qu' il vaille", "que nous valions", "que vous valiez", "qu' ils vaillent"],
        "conditionnel passé": ["j'aurais valu", "tu aurais valu", "il aurait valu", "nous aurions valu", "vous auriez valu", "ils auraient valu"],
        "futur antérieur": ["j'aurai valu", "tu auras valu", "il aura valu", "nous aurons valu", "vous aurez valu", "ils auront valu"]
    },
    'asseoir': {
        'présent': ['j\' assois', 'tu assois', 'il assoit', 'nous assoyons', 'vous assoyez', 'ils assoient'],
        'passé composé': ['j\' ai assis', 'tu as assis', 'il a assis', 'nous avons assis', 'vous avez assis', 'ils ont assis'],
        'imparfait': ['j\' assoyais', 'tu assoyais', 'il assoyait', 'nous assoyions', 'vous assoyiez', 'ils assoyaient'],
        'futur simple': ['j\' assoirai', 'tu assoiras', 'il assoira', 'nous assoirons', 'vous assoirez', 'ils assoiront'],
        'conditionnel présent': ['j\' assoirais', 'tu assoirais', 'il assoirait', 'nous assoirions', 'vous assoiriez', 'ils assoiraient'],
        'passé simple': ['j\' assus', 'tu assus', 'il assut', 'nous assûmes', 'vous assûtes', 'ils assurent'],
        "plus-que-parfait": ["j'avais assis", "tu avais assis", "il avait assis", "nous avions assis", "vous aviez assis", "ils avaient assis"],
        "subjonctif présent": ["que j'assoie", "que tu assoies", "qu' il assoie", "que nous assoyions", "que vous assoyiez", "qu' ils assoient"],
        "conditionnel passé": ["j'aurais assis", "tu aurais assis", "il aurait assis", "nous aurions assis", "vous auriez assis", "ils auraient assis"],
        "futur antérieur": ["j'aurai assis", "tu auras assis", "il aura assis", "nous aurons assis", "vous aurez assis", "ils auront assis"]
    },
    'craindre': {
        'présent': ['je crains', 'tu crains', 'il craint', 'nous craignons', 'vous craignez', 'ils craignent'],
        'passé composé': ['j\' ai craint', 'tu as craint', 'il a craint', 'nous avons craint', 'vous avez craint', 'ils ont craint'],
        'imparfait': ['je craignais', 'tu craignais', 'il craignait', 'nous craignions', 'vous craigniez', 'ils craignaient'],
        'futur simple': ['je craindrai', 'tu craindras', 'il craindra', 'nous craindrons', 'vous craindrez', 'ils craindront'],
        'conditionnel présent': ['je craindrais', 'tu craindrais', 'il craindrait', 'nous craindrions', 'vous craindriez', 'ils craindraient'],
        'passé simple': ['je craignis', 'tu craignis', 'il craignit', 'nous craignîmes', 'vous craignîtes', 'ils craignirent'],
        "plus-que-parfait": ["j'avais craint", "tu avais craint", "il avait craint", "nous avions craint", "vous aviez craint", "ils avaient craint"],
        "subjonctif présent": ["que je craigne", "que tu craignes", "qu' il craigne", "que nous craignions", "que vous craigniez", "qu' ils craignent"],
        "conditionnel passé": ["j'aurais craint", "tu aurais craint", "il aurait craint", "nous aurions craint", "vous auriez craint", "ils auraient craint"],
        "futur antérieur": ["j'aurai craint", "tu auras craint", "il aura craint", "nous aurons craint", "vous aurez craint", "ils auront craint"]
    },
    'plaire': {
        'présent': ['je plais', 'tu plais', 'il plaît', 'nous plaisons', 'vous plaisez', 'ils plaisent'],
        'passé composé': ['j\' ai plu', 'tu as plu', 'il a plu', 'nous avons plu', 'vous avez plu', 'ils ont plu'],
        'imparfait': ['je plaisais', 'tu plaisais', 'il plaisait', 'nous plaisions', 'vous plaisiez', 'ils plaisaient'],
        'futur simple': ['je plairai', 'tu plairas', 'il plaira', 'nous plairons', 'vous plairez', 'ils plairont'],
        'conditionnel présent': ['je plairais', 'tu plairais', 'il plairait', 'nous plairions', 'vous plairiez', 'ils plairaient'],
        'passé simple': ['je plus', 'tu plus', 'il plut', 'nous plûmes', 'vous plûtes', 'ils plurent'],
        "plus-que-parfait": ["j'avais plu", "tu avais plu", "il avait plu", "nous avions plu", "vous aviez plu", "ils avaient plu"],
        "subjonctif présent": ["que je plaise", "que tu plaises", "qu' il plaise", "que nous plaisions", "que vous plaisiez", "qu' ils plaisent"],
        "conditionnel passé": ["j'aurais plu", "tu aurais plu", "il aurait plu", "nous aurions plu", "vous auriez plu", "ils auraient plu"],
        "futur antérieur": ["j'aurai plu", "tu auras plu", "il aura plu", "nous aurons plu", "vous aurez plu", "ils auront plu"]
    }
}


verbes = list(conjugaisons.keys())

# Fonction pour choisir un verbe et un temps au hasard

utilise = set()
dernier_verbe = []
dernier_temps = []


def choisir_exercice():
    global utilise, dernier_verbe, dernier_temps

    combinaisons_possibles = [(verbe, temps)
                              for verbe in verbes for temps in conjugaisons[verbe]]

    if len(utilise) == len(combinaisons_possibles):
        utilise = set()
        dernier_verbe = []
        dernier_temps = []

    while True:
        verbe = random.choice(verbes)
        temps = random.choice(list(conjugaisons[verbe].keys()))
        if len(dernier_verbe) == len(list(conjugaisons.keys())):
            dernier_verbe = []

        if len(dernier_temps) == len(list(conjugaisons[verbe].keys())):
            dernier_temps = []

        if (verbe, temps) not in utilise and temps not in dernier_temps and verbe not in dernier_verbe:
            utilise.add((verbe, temps))
            dernier_verbe.append(verbe)
            dernier_temps.append(temps)
            return verbe, temps


def exercice():
    points = 0
    verbe, temps = choisir_exercice()
    print(f"Conjugue le verbe '{verbe}' au temps '{temps}':")

    # Afficher la réponse correcte pour chaque personne
    for i, personne in enumerate(['je', 'tu', 'il', 'nous', 'vous', 'ils']):
        reponse = input(f"{personne} : ")
        verification = conjugaisons[verbe][temps][i].split()
        print("verif:", verification)
        if len(verification) == 2:
            if reponse.strip().lower() == verification[1].lower():
                console.print("Correct!", style="bold green")
                points += 1
            else:
                console.print(
                    f"Incorrect. La bonne réponse est: {verification[1]}", style="bold red")
        elif len(verification) > 2:
            if temps.split()[0] != 'subjonctif':
                if reponse.strip().lower() == f'{verification[1].lower()} {verification[2].lower()}':
                    console.print("Correct!", style="bold green")
                    points += 1
                else:
                    console.print(
                        f"Incorrect. La bonne réponse est: {verification[1].lower()} {verification[2].lower()}", style="bold red")
            else:
                global subjonctif_input
                if verification[0].lower() == 'que':
                    subjonctif_input = f'{verification[0].lower()} {verification[1].lower()} {verification[2].lower()}'

                else:
                    subjonctif_input = f'{verification[0].lower()}{verification[1].lower()} {verification[2].lower()}'

                if reponse.strip().lower() == subjonctif_input:
                    console.print("Correct!", style="bold green")
                    points += 1
                else:
                    if verification[0].lower() == 'que':
                        console.print(
                            f"Incorrect. La bonne réponse est: {verification[0].lower()} {verification[1].lower()} {verification[2].lower()}", style="bold red")
                    else:
                        console.print(
                            f"Incorrect. La bonne réponse est: {verification[0].lower()}{verification[1].lower()} {verification[2].lower()}", style="bold red")

    return points


def main():
    try:
        goal = int(input(
            'Veuillez entrer le nombre de bonnes réponses requises pour terminer la session: '))
    except ValueError:
        print("Veuillez entrer un nombre valide")
    total_points = 0
    while total_points < goal:
        points = exercice()
        total_points += points
        console.print(
            f"Votre score actuel est : {total_points} points.", style="bold purple")
        if total_points >= goal:
            console.print(
                f"Félicitations, vous avez atteint {goal} points!", style="bold green")
            break


if __name__ == "__main__":
    main()
