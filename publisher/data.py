from sklearn.datasets import fetch_20newsgroups

interesting_categories = [
    'alt.atheism','comp.graphics','comp.os.ms-windows.misc',
    'comp.sys.ibm.pc.hardware','comp.sys.mac.hardware','comp.windows.x',
    'misc.forsale','rec.autos','rec.motorcycles','rec.sport.baseball'
]

not_interesting_categories = [
    'rec.sport.hockey','sci.crypt','sci.electronics','sci.med','sci.space',
    'soc.religion.christian','talk.politics.guns','talk.politics.mideast',
    'talk.politics.misc','talk.religion.misc'
]

interesting_data = {
    cat: fetch_20newsgroups(subset='all', categories=[cat], remove=('headers','footers','quotes')).data
    for cat in interesting_categories
}

not_interesting_data = {
    cat: fetch_20newsgroups(subset='all', categories=[cat], remove=('headers','footers','quotes')).data
    for cat in not_interesting_categories
}