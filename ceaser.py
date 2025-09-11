import numpy as np
import string

# Frequencies of letters a-z in English (approx. % values normalized)
letter_freq = np.array([
    0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015,
    0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
    0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
    0.00978, 0.02360, 0.00150, 0.01974, 0.00074
])

# The ciphertext
text = """Tyrgkvi 1

Yrggp wrdzczvj riv rcc rczbv; vmvip leyrggp wrdzcp zj leyrggp ze zkj fne
nrp.

Vmvipkyzex nrj ze tfewljzfe ze kyv Fscfejbpj’ yfljv. Kyv nzwv yru
uzjtfmvivu kyrk kyv yljsreu nrj triipzex fe re zekizxlv nzky r Wivety
xzic, nyf yru svve r xfmvievjj ze kyvzi wrdzcp, reu jyv yru reefletvu kf
yvi yljsreu kyrk jyv tflcu efk xf fe czmzex ze kyv jrdv yfljv nzky yzd.
Kyzj gfjzkzfe fw rwwrzij yru efn crjkvu kyivv urpj, reu efk fecp kyv
yljsreu reu nzwv kyvdjvcmvj, slk rcc kyv dvdsvij fw kyvzi wrdzcp reu
yfljvyfcu, nviv grzewlccp tfejtzflj fw zk. Vmvip gvijfe ze kyv yfljv
wvck kyrk kyviv nrj ef jvejv ze kyvzi czmzex kfxvkyvi, reu kyrk kyv
jkirp gvfgcv siflxyk kfxvkyvi sp tyretv ze rep zee yru dfiv ze tfddfe
nzky fev refkyvi kyre kyvp, kyv dvdsvij fw kyv wrdzcp reu yfljvyfcu fw
kyv Fscfejbpj. Kyv nzwv uzu efk cvrmv yvi fne iffd, kyv yljsreu yru efk
svve rk yfdv wfi kyivv urpj. Kyv tyzcuive ire nzcu rcc fmvi kyv yfljv;
kyv Vexczjy xfmvievjj hlriivcvu nzky kyv yfljvbvvgvi, reu nifkv kf r
wizveu rjbzex yvi kf cffb flk wfi r evn jzklrkzfe wfi yvi; kyv dre-tffb
yru nrcbvu wfi kyv urp svwfiv aljk rk uzeevi kzdv; kyv bzktyve-drzu, reu

kyv tfrtydre yru xzmve nriezex.

Kyivv urpj rwkvi kyv hlriivc, Gizetv Jkvgre Ribrupvmzkty Fscfejbp—Jkzmr,
rj yv nrj trccvu ze kyv wrjyzferscv nficu—nfbv lg rk yzj ljlrc yfli,
kyrk zj, rk vzxyk f’tcftb ze kyv dfiezex, efk ze yzj nzwv’j svuiffd, slk
fe kyv cvrkyvi-tfmvivu jfwr ze yzj jklup. Yv klievu fmvi yzj jkflk,
nvcc-trivu-wfi gvijfe fe kyv jgizexp jfwr, rj kyflxy yv nflcu jzeb zekf
r cfex jcvvg rxrze; yv mzxfifljcp vdsirtvu kyv gzccfn fe kyv fkyvi jzuv
reu slizvu yzj wrtv ze zk; slk rcc rk fetv yv aldgvu lg, jrk lg fe kyv
jfwr, reu fgvevu yzj vpvj.

&quot;Pvj, pvj, yfn nrj zk efn?&quot; yv kyflxyk, xfzex fmvi yzj uivrd. &quot;Efn, yfn
nrj zk? Kf sv jliv! Rcrsze nrj xzmzex r uzeevi rk Uridjkruk; ef, efk
Uridjkruk, slk jfdvkyzex Rdviztre. Pvj, slk kyve, Uridjkruk nrj ze
Rdviztr. Pvj, Rcrsze nrj xzmzex r uzeevi fe xcrjj krscvj, reu kyv krscvj
jrex, _Zc dzf kvjfif_—efk _Zc dzf kvjfif_ kyflxy, slk jfdvkyzex svkkvi,
reu kyviv nviv jfdv jfik fw czkkcv uvtrekvij fe kyv krscv, reu kyvp nviv
nfdve, kff,&quot; yv ivdvdsvivu.

Jkvgre Ribrupvmzkty’j vpvj knzebcvu xrzcp, reu yv gfeuvivu nzky r jdzcv.
&quot;Pvj, zk nrj eztv, mvip eztv. Kyviv nrj r xivrk uvrc dfiv kyrk nrj
uvczxykwlc, fecp kyviv’j ef glkkzex zk zekf nfiuj, fi vmve vogivjjzex zk
ze fev’j kyflxykj rnrbv.&quot; Reu efkztzex r xcvrd fw czxyk gvvgzex ze
svjzuv fev fw kyv jvixv tlikrzej, yv tyvviwlccp uifggvu yzj wvvk fmvi
kyv vuxv fw kyv jfwr, reu wvck rsflk nzky kyvd wfi yzj jczggvij, r
givjvek fe yzj crjk szikyurp, nfibvu wfi yzd sp yzj nzwv fe xfcu-tfcfivu
dfifttf. Reu, rj yv yru ufev vmvip urp wfi kyv crjk ezev pvrij, yv
jkivktyvu flk yzj yreu, nzkyflk xvkkzex lg, kfnriuj kyv gcrtv nyviv yzj
uivjjzex-xfne rcnrpj ylex ze yzj svuiffd. Reu kyvivlgfe yv jluuvecp
ivdvdsvivu kyrk yv nrj efk jcvvgzex ze yzj nzwv’j iffd, slk ze yzj

jklup, reu nyp: kyv jdzcv mrezjyvu wifd yzj wrtv, yv bezkkvu yzj sifnj.

&quot;Ry, ry, ry! Ff!...&quot; yv dlkkvivu, ivtrcczex vmvipkyzex kyrk yru
yrggvevu. Reu rxrze vmvip uvkrzc fw yzj hlriivc nzky yzj nzwv nrj
givjvek kf yzj zdrxzerkzfe, rcc kyv yfgvcvjjevjj fw yzj gfjzkzfe, reu
nfijk fw rcc, yzj fne wrlck.

&quot;Pvj, jyv nfe’k wfixzmv dv, reu jyv tre’k wfixzmv dv. Reu kyv dfjk rnwlc
kyzex rsflk zk zj kyrk zk’j rcc dp wrlck—rcc dp wrlck, kyflxy Z’d efk kf
scrdv. Kyrk’j kyv gfzek fw kyv nyfcv jzklrkzfe,&quot; yv ivwcvtkvu. &quot;Fy, fy,
fy!&quot; yv bvgk ivgvrkzex ze uvjgrzi, rj yv ivdvdsvivu kyv rtlkvcp grzewlc
jvejrkzfej trljvu yzd sp kyzj hlriivc.

Dfjk legcvrjrek fw rcc nrj kyv wzijk dzelkv nyve, fe tfdzex, yrggp reu
xffu-yldfivu, wifd kyv kyvrkvi, nzky r ylxv gvri ze yzj yreu wfi yzj
nzwv, yv yru efk wfleu yzj nzwv ze kyv uirnzex-iffd, kf yzj jligizjv yru
efk wfleu yvi ze kyv jklup vzkyvi, reu jrn yvi rk crjk ze yvi svuiffd
nzky kyv lecltbp cvkkvi kyrk ivmvrcvu vmvipkyzex ze yvi yreu.

Jyv, yzj Ufccp, wfivmvi wljjzex reu nfiipzex fmvi yfljvyfcu uvkrzcj, reu
czdzkvu ze yvi zuvrj, rj yv tfejzuvivu, nrj jzkkzex gviwvtkcp jkzcc nzky
kyv cvkkvi ze yvi yreu, cffbzex rk yzd nzky re vogivjjzfe fw yfiifi,
uvjgrzi, reu zeuzxerkzfe.

&quot;Nyrk’j kyzj? kyzj?&quot; jyv rjbvu, gfzekzex kf kyv cvkkvi.

Reu rk kyzj ivtfccvtkzfe, Jkvgre Ribrupvmzkty, rj zj jf fwkve kyv trjv,
nrj efk jf dlty reefpvu rk kyv wrtk zkjvcw rj rk kyv nrp ze nyzty yv yru
dvk yzj nzwv’j nfiuj.

Kyviv yrggvevu kf yzd rk kyrk zejkrek nyrk ufvj yrggve kf gvfgcv nyve
kyvp riv levogvtkvucp trlxyk ze jfdvkyzex mvip uzjxirtvwlc. Yv uzu efk
jlttvvu ze rurgkzex yzj wrtv kf kyv gfjzkzfe ze nyzty yv nrj gcrtvu
kfnriuj kyzj nzwv sp kyv uzjtfmvipy fw yzj wrlck. Zejkvru fw svzex ylik,
uvepzex, uvwveuzex yzdjvcw, svxxzex wfixzmvevjj, zejkvru fw ivdrzezex
zeuzwwvivek vmve—repkyzex nflcu yrmv svve svkkvi kyre nyrk yv uzu uf—yzj
wrtv lkkvicp zemfclekrizcp (ivwcvo jgzerc rtkzfe, ivwcvtkvu Jkvgre
Ribrupvmzkty, nyf nrj wfeu fw gypjzfcfxp)—lkkvicp zemfclekrizcp rjjldvu
zkj yrszklrc, xffu-yldfivu, reu kyvivwfiv zuzfkzt jdzcv.

Kyzj zuzfkzt jdzcv yv tflcu efk wfixzmv yzdjvcw. Trktyzex jzxyk fw kyrk
jdzcv, Ufccp jyluuvivu rj kyflxy rk gypjztrc grze, sifbv flk nzky yvi
tyrirtkvizjkzt yvrk zekf r wcffu fw tilvc nfiuj, reu iljyvu flk fw kyv
iffd. Jzetv kyve jyv yru ivwljvu kf jvv yvi yljsreu.

&quot;Zk’j kyrk zuzfkzt jdzcv kyrk’j kf scrdv wfi zk rcc,&quot; kyflxyk Jkvgre
Ribrupvmzkty.

&quot;Slk nyrk’j kf sv ufev? Nyrk’j kf sv ufev?&quot; yv jrzu kf yzdjvcw ze
uvjgrzi, reu wfleu ef rejnvi."""

# Lowercase the text
text = text.lower()

# Define the alphabet
abc = list(string.ascii_lowercase)

# Count frequency of letters in text
freq = np.zeros(26)
for char in text:
    if char in abc:
        freq[abc.index(char)] += 1
freq /= freq.sum()  # Normalize

# Compute error for each possible shift
error = [0] * 26
for i in range(26):
    # Shift the English frequencies to align with the ciphertext
    rolled_english_freq = np.roll(letter_freq, -i)
    error[i] = np.sum(np.abs(freq - rolled_english_freq))

# Find shift with minimal error
min_index = 26 - error.index(min(error))
print("Best shift:", min_index)

# Decrypt the text using the Caesar cipher shift
decrypted_text = ""
for char in text:
    if char in abc:
        # Find the index of the character in the alphabet
        char_index = abc.index(char)
        # Apply the decryption shift (subtract min_index)
        new_index = (char_index - min_index) % 26
        decrypted_text += abc[new_index]
    else:
        # Keep non-letter characters unchanged
        decrypted_text += char

# Print the decrypted text
print("\nDecrypted text:")
print(decrypted_text)