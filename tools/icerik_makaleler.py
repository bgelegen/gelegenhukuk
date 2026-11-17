# -*- coding: utf-8 -*-
"""
Makale içerikleri. Yeni yazı eklemek için listeye bir sözlük ekleyip
`python3 tools/uret.py` çalıştırmanız yeterli (ardından CSP hash'lerini yenileyin).
'cat' değeri icerik_alanlar.py'deki 'kategori' ile eşleşmelidir.
Dil: yalnızca bilgilendirici; reklam yasağına uygun.
"""

MAKALELER = [
  # ------------------------------------------------------------------ AİLE
  {
    "slug": "anlasmali-bosanma-nasil-yapilir.html",
    "cat": "Aile Hukuku", "tarih": "2026-11-17", "read": "5 dk okuma",
    "title": "Anlaşmalı Boşanma Nasıl Yapılır? | Gelegen Hukuk Bürosu",
    "desc": "Anlaşmalı boşanmanın şartları, gerekli belgeler, boşanma protokolünde yer alması gereken konular ve süreç. Malatya Gelegen Hukuk Bürosu bilgilendirme yazısı.",
    "h1": "Anlaşmalı Boşanma Nasıl Yapılır?",
    "lead": "Eşlerin boşanma ve sonuçları üzerinde anlaştığı durumlarda anlaşmalı boşanma, en hızlı ve en az yıpratıcı yoldur. Bu yazıda şartları, gerekli belgeleri ve süreci özetliyoruz.",
    "body": """
          <h2>Anlaşmalı boşanmanın şartları</h2>
          <p>Türk Medeni Kanunu m. 166/3 uyarınca anlaşmalı boşanmaya karar verilebilmesi için üç temel koşul aranır:</p>
          <ul>
            <li>Evliliğin <strong>en az bir yıl</strong> sürmüş olması,</li>
            <li>Eşlerin <strong>birlikte</strong> başvurması ya da bir eşin açtığı davayı diğerinin kabul etmesi,</li>
            <li>Hâkimin tarafları bizzat dinleyerek iradelerin serbestçe açıklandığına kanaat getirmesi.</li>
          </ul>
          <p>Bu şartlardan biri karşılanmıyorsa boşanma, çekişmeli boşanma usulüne göre yürür.</p>

          <h2>Boşanma protokolü nedir, neler yer almalı?</h2>
          <p>Anlaşmalı boşanmanın özü, tarafların boşanmanın malî ve kişisel sonuçları üzerinde yazılı olarak anlaştığı <strong>boşanma protokolü</strong>dür. Hâkimin protokolü onaylaması için uyuşmazlık doğurabilecek tüm konuların açıkça düzenlenmiş olması gerekir:</p>
          <ul>
            <li><strong>Velayet:</strong> Ortak çocuğun velayetinin kime bırakılacağı,</li>
            <li><strong>Kişisel ilişki:</strong> Velayeti almayan eşin çocukla göreceği günler ve koşullar,</li>
            <li><strong>İştirak nafakası:</strong> Çocuğun giderlerine katkı payı,</li>
            <li><strong>Yoksulluk nafakası:</strong> Boşanma yüzünden yoksulluğa düşecek eş için nafaka olup olmayacağı,</li>
            <li><strong>Maddi ve manevi tazminat</strong> talepleri,</li>
            <li><strong>Mal paylaşımı:</strong> Edinilmiş mallara ilişkin düzenleme ya da ayrı dava saklı tutulacaksa bunun belirtilmesi.</li>
          </ul>

          <h2>Gerekli belgeler</h2>
          <ul>
            <li>Tarafların kimlik belgeleri,</li>
            <li>Taraflarca imzalanmış boşanma protokolü,</li>
            <li>Dava dilekçesi,</li>
            <li>Varsa vekâletname (avukatla takip ediliyorsa).</li>
          </ul>

          <h2>Süreç ne kadar sürer?</h2>
          <p>Anlaşmalı boşanma genellikle <strong>tek duruşmada</strong> sonuçlanır. Her iki eşin de duruşmada hazır bulunup iradesini beyan etmesi zorunludur; bu beyan vekâletle değil, eşin kendisi tarafından yapılır. Kararın yazılması, tebliği ve kesinleşmesiyle süreç tamamlanır. Uygulamada başvurudan kesinleşmeye kadar geçen süre mahkemenin yoğunluğuna göre değişir.</p>

          <h2>Sık yapılan hatalar</h2>
          <ul>
            <li>Protokolde mal paylaşımının belirsiz bırakılması — ileride ayrı bir mal rejimi davasına yol açabilir.</li>
            <li>Nafaka miktarının güncellenme koşuluna yer verilmemesi.</li>
            <li>Çocukla kişisel ilişkinin genel ifadelerle yazılması — uygulamada anlaşmazlık doğurur.</li>
          </ul>
""",
  },
  {
    "slug": "cekismeli-bosanma-davasi.html",
    "cat": "Aile Hukuku", "tarih": "2026-11-17", "read": "6 dk okuma",
    "title": "Çekişmeli Boşanma Davası: Sebepler ve Süreç | Gelegen Hukuk Bürosu",
    "desc": "Çekişmeli boşanma davasının sebepleri (TMK 161-166), hak düşürücü süreler, deliller, tanıklar ve yargılama süreci. Malatya Gelegen Hukuk Bürosu bilgilendirme yazısı.",
    "h1": "Çekişmeli Boşanma Davası: Sebepler ve Süreç",
    "lead": "Eşler boşanmanın kendisi veya sonuçları (velayet, nafaka, tazminat, mal paylaşımı) konusunda anlaşamıyorsa boşanma çekişmeli dava yoluyla görülür. Bu yazıda boşanma sebeplerini ve davanın nasıl ilerlediğini özetliyoruz.",
    "body": """
          <h2>Boşanma sebepleri nelerdir?</h2>
          <p>Türk Medeni Kanunu, boşanma sebeplerini <strong>özel</strong> ve <strong>genel</strong> sebepler olarak ikiye ayırır.</p>
          <h3>Özel boşanma sebepleri</h3>
          <ul>
            <li><strong>Zina</strong> (TMK m. 161),</li>
            <li><strong>Hayata kast, pek kötü veya onur kırıcı davranış</strong> (TMK m. 162),</li>
            <li><strong>Suç işleme ve haysiyetsiz hayat sürme</strong> (TMK m. 163),</li>
            <li><strong>Terk</strong> (TMK m. 164),</li>
            <li><strong>Akıl hastalığı</strong> (TMK m. 165).</li>
          </ul>
          <h3>Genel boşanma sebepleri</h3>
          <ul>
            <li><strong>Evlilik birliğinin temelinden sarsılması</strong> (TMK m. 166/1): Ortak hayatın sürdürülemeyecek ölçüde sarsılması. Uygulamada en sık başvurulan sebeptir.</li>
            <li><strong>Fiilî ayrılık</strong> (TMK m. 166/4): Daha önce açılan boşanma davasının reddedilip kesinleşmesinden itibaren üç yıl geçtiği hâlde ortak hayatın yeniden kurulamaması.</li>
          </ul>

          <h2>Hak düşürücü sürelere dikkat</h2>
          <p>Zina ile hayata kast, pek kötü veya onur kırıcı davranış sebeplerine dayanan davalar, sebebin öğrenilmesinden itibaren <strong>altı ay</strong> ve her hâlde olayın üzerinden <strong>beş yıl</strong> geçmekle açılamaz. Affeden eşin dava hakkı da yoktur. Terk sebebinde ise terkin en az altı ay sürmüş olması ve usulüne uygun ihtar yapılması gerekir.</p>

          <h2>Davada kusur ve deliller</h2>
          <p>Çekişmeli boşanmada tarafların kusur durumu; tazminat ve yoksulluk nafakası gibi taleplerin kabulünü doğrudan etkiler. Bu nedenle iddiaların ispatı önemlidir. Başlıca deliller şunlardır:</p>
          <ul>
            <li>Tanık beyanları,</li>
            <li>Yazışmalar ve mesaj kayıtları (hukuka uygun elde edilmiş olmak şartıyla),</li>
            <li>Hastane ve darp raporları, kolluk kayıtları,</li>
            <li>Banka kayıtları ve diğer resmî belgeler.</li>
          </ul>

          <h2>Yargılama nasıl ilerler?</h2>
          <ol>
            <li><strong>Dilekçeler aşaması:</strong> Dava, cevap, cevaba cevap ve ikinci cevap dilekçeleri karşılıklı verilir.</li>
            <li><strong>Ön inceleme:</strong> Uyuşmazlık konuları belirlenir, taraflar sulhe teşvik edilir.</li>
            <li><strong>Tahkikat:</strong> Tanıklar dinlenir, deliller toplanır; çocuk varsa sosyal inceleme raporu alınabilir.</li>
            <li><strong>Karar:</strong> Boşanma ile birlikte velayet, nafaka ve tazminat hakkında hüküm kurulur.</li>
            <li><strong>Kanun yolları:</strong> Karar, istinaf ve temyiz yoluyla denetlenebilir.</li>
          </ol>

          <h2>Dava sürerken alınabilecek tedbirler</h2>
          <p>Dava açılınca hâkim, yargılama süresince gerekli geçici önlemleri kendiliğinden alır (TMK m. 169). Eşlerin barınması, geçimi, malların yönetimi ve çocukların bakımı bu kapsamdadır. Tedbir nafakası ve çocukla geçici kişisel ilişki bu yolla düzenlenir.</p>
""",
  },
  {
    "slug": "nafaka-turleri.html",
    "cat": "Aile Hukuku", "tarih": "2026-11-17", "read": "5 dk okuma",
    "title": "Nafaka Türleri: Tedbir, İştirak ve Yoksulluk Nafakası | Gelegen Hukuk Bürosu",
    "desc": "Tedbir, iştirak, yoksulluk ve yardım nafakası nedir, kimler talep edebilir, nafaka nasıl artırılır veya kaldırılır? Malatya Gelegen Hukuk Bürosu bilgilendirme yazısı.",
    "h1": "Nafaka Türleri: Tedbir, İştirak ve Yoksulluk Nafakası",
    "lead": "Nafaka, boşanma sürecinde ve sonrasında eşlerin ve çocukların geçimini güvence altına alan bir ödeme yükümlülüğüdür. Bu yazıda nafaka türlerini, şartlarını ve sonradan değiştirilmesini özetliyoruz.",
    "body": """
          <h2>1. Tedbir nafakası</h2>
          <p>Boşanma veya ayrılık davası süresince, eşin ve çocukların geçimi için hükmedilen geçici nafakadır (TMK m. 169). Dava açılmadan önce, birlikte yaşamaya ara verilmesi hâlinde de istenebilir (TMK m. 197). Kusur şartı aranmaz; ihtiyaç ve tarafların ekonomik durumu belirleyicidir.</p>

          <h2>2. İştirak nafakası</h2>
          <p>Velayet kendisine verilmeyen ebeveynin, çocuğun bakım ve eğitim giderlerine gücü oranında katılması için ödediği nafakadır (TMK m. 182). Çocuğun ergin olmasına (kural olarak 18 yaş) kadar devam eder; çocuğun eğitimi devam ediyorsa ergin olduktan sonra <strong>yardım nafakası</strong> gündeme gelebilir.</p>

          <h2>3. Yoksulluk nafakası</h2>
          <p>Boşanma yüzünden yoksulluğa düşecek eşin, kusuru daha ağır olmamak şartıyla diğer eşten süresiz olarak talep edebildiği nafakadır (TMK m. 175). Nafaka yükümlüsünün kusuru aranmaz. Yoksulluk nafakası boşanma kararıyla birlikte istenmemişse, karar kesinleştikten sonra <strong>bir yıl</strong> içinde ayrı bir davayla talep edilebilir (TMK m. 178).</p>

          <h2>4. Yardım nafakası</h2>
          <p>Yardım edilmediği takdirde yoksulluğa düşecek olan üstsoy, altsoy ve kardeşlerin, kanunda sayılan akrabalarından talep edebildiği nafakadır (TMK m. 364). Ergin olmasına rağmen eğitimi süren çocuk, eğitimi bitinceye kadar ana babasından bu yolla nafaka isteyebilir.</p>

          <h2>Nafaka miktarı nasıl belirlenir?</h2>
          <p>Mahkeme; tarafların gelirleri, giderleri, sosyal ve ekonomik durumları ile çocukların ihtiyaçlarını birlikte değerlendirir. Kararda nafakanın her yıl hangi oranda artırılacağı da belirtilebilir; uygulamada çoğunlukla Türkiye İstatistik Kurumu tarafından açıklanan <strong>ÜFE/TÜFE oranları</strong> esas alınır.</p>

          <h2>Nafaka artırılabilir, azaltılabilir veya kaldırılabilir mi?</h2>
          <ul>
            <li>Tarafların mali durumlarının değişmesi veya hakkaniyetin gerektirmesi hâlinde nafakanın <strong>artırılması veya azaltılması</strong> istenebilir (TMK m. 176).</li>
            <li>Nafaka alacaklısının yeniden evlenmesi veya taraflardan birinin ölümüyle yoksulluk nafakası kendiliğinden kalkar.</li>
            <li>Alacaklının evlenmeksizin fiilen evliymiş gibi yaşaması, yoksulluğunun sona ermesi veya haysiyetsiz hayat sürmesi hâlinde nafakanın kaldırılması mahkemeden istenebilir.</li>
          </ul>

          <h2>Nafaka ödenmezse ne olur?</h2>
          <p>Nafaka kararı ilamlı icra yoluyla takip edilebilir. Ayrıca nafaka borcunu ödemeyen kişi hakkında, alacaklının şikâyeti üzerine İcra ve İflas Kanunu m. 344 uyarınca <strong>üç aya kadar tazyik hapsi</strong> uygulanabilir.</p>
""",
  },
  {
    "slug": "velayet-davasi.html",
    "cat": "Aile Hukuku", "tarih": "2026-11-17", "read": "5 dk okuma",
    "title": "Velayet Davası: Velayet Kime Verilir, Nasıl Değiştirilir? | Gelegen Hukuk Bürosu",
    "desc": "Boşanmada velayetin belirlenmesi, çocuğun üstün yararı, sosyal inceleme raporu, ortak velayet ve velayetin değiştirilmesi davası. Malatya Gelegen Hukuk Bürosu bilgilendirme yazısı.",
    "h1": "Velayet Davası: Velayet Kime Verilir, Nasıl Değiştirilir?",
    "lead": "Boşanma sürecinin en hassas konusu çoğu zaman çocukların velayetidir. Bu yazıda mahkemenin velayet kararında neleri dikkate aldığını ve velayetin sonradan nasıl değiştirilebileceğini özetliyoruz.",
    "body": """
          <h2>Velayet nedir?</h2>
          <p>Velayet, ergin olmayan çocuğun bakımı, eğitimi, korunması ve temsili konusunda ana ve babaya tanınan hak ve yükümlülüklerin bütünüdür (TMK m. 335 vd.). Evlilik devam ederken velayeti ana ve baba birlikte kullanır; boşanmada ise hâkim velayeti kural olarak eşlerden birine verir.</p>

          <h2>Mahkeme velayet kararında neleri dikkate alır?</h2>
          <p>Velayet kararında tek ve belirleyici ölçüt <strong>çocuğun üstün yararıdır</strong>. Mahkeme bu değerlendirmeyi yaparken şu unsurlara bakar:</p>
          <ul>
            <li>Çocuğun yaşı, cinsiyeti ve bakım ihtiyacı,</li>
            <li>Ebeveynlerin yaşam koşulları, çalışma düzeni ve çocuğa ayırabilecekleri zaman,</li>
            <li>Çocuğun alıştığı çevre, okul ve kardeşlerle birlikte kalma imkânı,</li>
            <li><strong>İdrak çağındaki çocuğun görüşü,</strong></li>
            <li>Uzman (pedagog, psikolog, sosyal çalışmacı) tarafından hazırlanan <strong>sosyal inceleme raporu</strong>.</li>
          </ul>
          <p>Küçük yaştaki çocukların velayetinin, aksini gerektiren bir durum yoksa genellikle anneye verildiği görülmektedir; ancak bu bir kanun kuralı değil, her somut olayda ayrıca değerlendirilen bir durumdur.</p>

          <h2>Ortak velayet mümkün mü?</h2>
          <p>Yargıtay'ın son yıllardaki kararlarında, tarafların anlaşması ve çocuğun yararına uygun olması şartıyla boşanmada <strong>ortak velayet</strong> kararı verilebileceği kabul edilmektedir. Ortak velayet, özellikle anlaşmalı boşanmalarda protokolle düzenlenebilir.</p>

          <h2>Velayeti almayan ebeveynin hakları</h2>
          <p>Velayet kendisine verilmeyen ebeveyn ile çocuk arasında <strong>kişisel ilişki</strong> kurulur; mahkeme görüşme günlerini, saatlerini ve tatil dönemlerini kararında belirler. Bu ebeveyn ayrıca çocuğun giderlerine <strong>iştirak nafakası</strong> ile katılır.</p>

          <h2>Velayetin değiştirilmesi</h2>
          <p>Boşanmadan sonra durumların önemli ölçüde değişmesi hâlinde velayetin değiştirilmesi istenebilir (TMK m. 183). Örneğin:</p>
          <ul>
            <li>Velayet sahibi ebeveynin çocuğun bakımını ihmal etmesi,</li>
            <li>Kişisel ilişki kurulmasının sürekli engellenmesi,</li>
            <li>Çocuğun sağlığını veya gelişimini tehlikeye düşüren yaşam koşulları,</li>
            <li>Çocuğun, idrak çağına geldikten sonra diğer ebeveynle kalmak istemesi.</li>
          </ul>
          <p>Velayetin değiştirilmesi davası, çocuğun yerleşim yeri aile mahkemesinde açılır.</p>
""",
  },
  # ------------------------------------------------------------------ İŞ
  {
    "slug": "ise-iade-davasi-sartlar-sureler.html",
    "cat": "İş Hukuku", "tarih": "2026-11-17", "read": "6 dk okuma",
    "title": "İşe İade Davası: Şartlar ve Süreler | Gelegen Hukuk Bürosu",
    "desc": "İşe iade davasının şartları, 30 iş günü ve 1 aylık başvuru süreleri, zorunlu arabuluculuk ve işe başlatmama tazminatı. Malatya Gelegen Hukuk Bürosu bilgilendirme yazısı.",
    "h1": "İşe İade Davası: Şartlar ve Süreler",
    "lead": "İş sözleşmesi geçerli bir neden gösterilmeden feshedilen işçi, belirli şartlar altında işe iadesini talep edebilir. Süreç sıkı sürelere bağlıdır; bu yazıda şartları ve süreleri özetliyoruz.",
    "body": """
          <h2>İşe iade davasının şartları</h2>
          <p>İş Kanunu m. 18 ve devamı uyarınca iş güvencesi hükümlerinden yararlanıp işe iade talep edebilmek için şu koşulların birlikte bulunması gerekir:</p>
          <ul>
            <li>İş yerinde <strong>en az 30 işçi</strong> çalışıyor olması,</li>
            <li>İşçinin o iş yerindeki kıdeminin <strong>en az 6 ay</strong> olması,</li>
            <li>İş sözleşmesinin <strong>belirsiz süreli</strong> olması,</li>
            <li>Feshin işveren tarafından <strong>geçerli bir nedene dayanmadan</strong> yapılmış olması,</li>
            <li>İşçinin işveren vekili niteliğinde olmaması.</li>
          </ul>

          <h2>Önce zorunlu arabuluculuk</h2>
          <p>İşe iade talebinde <strong>dava açmadan önce arabulucuya başvurmak zorunludur</strong>. İşçi, fesih bildiriminin kendisine tebliğinden itibaren <strong>bir ay</strong> içinde arabulucuya başvurmalıdır. Taraflar arabuluculukta anlaşamazsa, son tutanağın düzenlendiği tarihten itibaren <strong>iki hafta</strong> içinde iş mahkemesinde dava açılır.</p>
          <div class="article-note">
            <p><strong>Dikkat:</strong> Bir aylık arabuluculuk başvuru süresi hak düşürücü niteliktedir. Süre kaçırılırsa işe iade hakkı ortadan kalkar.</p>
          </div>

          <h2>Dava sonunda ne olur?</h2>
          <p>Mahkeme feshi geçersiz bulursa işçinin işe iadesine karar verir. Kararın kesinleşmesinden sonra işçi <strong>10 iş günü</strong> içinde işverene başvurarak işe başlamak istediğini bildirmelidir.</p>
          <ul>
            <li><strong>İşveren işe başlatırsa:</strong> İşçiye boşta geçen süre için en çok 4 aya kadar ücret ve diğer hakları ödenir.</li>
            <li><strong>İşveren işe başlatmazsa:</strong> Kıdemine göre 4–8 aylık ücreti tutarında <strong>işe başlatmama tazminatı</strong> ile boşta geçen süre ücreti ödenir.</li>
          </ul>

          <h2>Hangi haklar saklı kalır?</h2>
          <p>İşe iade süreci; kıdem tazminatı, ihbar tazminatı, fazla mesai ve yıllık izin ücreti gibi işçilik alacaklarını ortadan kaldırmaz. Bu alacaklar ayrıca talep edilebilir.</p>
""",
  },
  {
    "slug": "kidem-tazminati-sartlari.html",
    "cat": "İş Hukuku", "tarih": "2026-11-17", "read": "6 dk okuma",
    "title": "Kıdem Tazminatı Şartları ve Hesaplanması | Gelegen Hukuk Bürosu",
    "desc": "Kıdem tazminatına hak kazanma şartları, istifa eden işçinin durumu, hesaplama yöntemi, tavan, zamanaşımı ve arabuluculuk. Malatya Gelegen Hukuk Bürosu bilgilendirme yazısı.",
    "h1": "Kıdem Tazminatı Şartları ve Hesaplanması",
    "lead": "Kıdem tazminatı, belirli bir süre çalışmış işçinin iş sözleşmesi kanunda sayılan sebeplerle sona erdiğinde işveren tarafından ödenen bir tazminattır. Bu yazıda hangi durumlarda kıdem tazminatı alınabileceğini ve nasıl hesaplandığını özetliyoruz.",
    "body": """
          <h2>Kıdem tazminatına hak kazanma şartları</h2>
          <p>Kıdem tazminatı, 1475 sayılı İş Kanunu'nun yürürlükte bırakılan 14. maddesinde düzenlenmiştir. Hak kazanmak için:</p>
          <ul>
            <li>İşçinin aynı işverene bağlı olarak <strong>en az bir yıl</strong> çalışmış olması,</li>
            <li>İş sözleşmesinin kanunda sayılan sebeplerden biriyle sona ermesi gerekir.</li>
          </ul>

          <h2>Hangi fesih hâllerinde kıdem tazminatı ödenir?</h2>
          <ul>
            <li>İşverenin, ahlak ve iyi niyet kurallarına uymayan hâller dışındaki bir sebeple iş sözleşmesini <strong>feshetmesi</strong>,</li>
            <li>İşçinin <strong>haklı nedenle</strong> sözleşmeyi feshetmesi (ör. ücretin ödenmemesi, SGK priminin eksik yatırılması, mobbing),</li>
            <li>Erkek işçinin <strong>muvazzaf askerlik</strong> nedeniyle ayrılması,</li>
            <li><strong>Emeklilik</strong> veya yaş dışındaki şartları tamamlayıp yaşlılık aylığı için gerekli prim gün sayısını ve sigortalılık süresini doldurma,</li>
            <li>Kadın işçinin <strong>evlendiği tarihten itibaren bir yıl içinde</strong> kendi isteğiyle ayrılması,</li>
            <li>İşçinin <strong>ölümü</strong> (tazminat mirasçılarına ödenir).</li>
          </ul>
          <p>Kural olarak sebepsiz istifa eden işçi kıdem tazminatı alamaz.</p>

          <h2>Kıdem tazminatı nasıl hesaplanır?</h2>
          <p>İşçiye, her tam hizmet yılı için <strong>30 günlük brüt ücreti</strong> tutarında kıdem tazminatı ödenir; bir yıldan artan süreler de oranlanarak hesaba katılır. Hesaplamada çıplak ücrete; düzenli olarak ödenen yol, yemek, ikramiye gibi para veya parayla ölçülebilen menfaatler de eklenir (<strong>giydirilmiş ücret</strong>).</p>
          <p>Bir yıllık hizmet için ödenecek kıdem tazminatı, kamu görevlileri için belirlenen <strong>kıdem tazminatı tavanını</strong> aşamaz. Tavan tutarı her yıl iki kez güncellenir. Kıdem tazminatından yalnızca damga vergisi kesilir.</p>

          <h2>Zamanaşımı ve faiz</h2>
          <p>Kıdem tazminatı alacağı, iş sözleşmesinin sona ermesinden itibaren <strong>beş yıllık</strong> zamanaşımına tabidir. Kıdem tazminatının zamanında ödenmemesi hâlinde, bankalarca mevduata uygulanan en yüksek faiz oranında faiz istenebilir.</p>

          <h2>Dava öncesi arabuluculuk</h2>
          <p>Kıdem tazminatı talepleri için dava açmadan önce <strong>arabulucuya başvurmak zorunludur</strong>. Arabuluculuk görüşmelerinde anlaşma sağlanırsa, anlaşma tutanağı ilam niteliğinde belge sayılır ve anlaşılan konular hakkında sonradan dava açılamaz.</p>
""",
  },
  # ------------------------------------------------------------------ İCRA
  {
    "slug": "icra-takibine-itiraz-nasil-yapilir.html",
    "cat": "İcra ve İflas Hukuku", "tarih": "2026-11-17", "read": "5 dk okuma",
    "title": "İcra Takibine İtiraz Nasıl Yapılır? | Gelegen Hukuk Bürosu",
    "desc": "Ödeme emrine itiraz süresi (7 gün), itirazın sonuçları, itirazın iptali ve kaldırılması davaları. Malatya Gelegen Hukuk Bürosu bilgilendirme yazısı.",
    "h1": "İcra Takibine İtiraz Nasıl Yapılır?",
    "lead": "Hakkınızda icra takibi başlatılıp ödeme emri tebliğ edildiğinde, borcu kabul etmiyorsanız yasal süresi içinde itiraz etmeniz gerekir. Süre çok kısadır; bu yazıda itiraz yolunu özetliyoruz.",
    "body": """
          <h2>Ödeme emrine itiraz süresi: 7 gün</h2>
          <p>İlamsız icra takibinde borçluya <strong>ödeme emri</strong> tebliğ edilir. Borçlu, tebliğ tarihinden itibaren <strong>7 gün</strong> içinde takibi yapan icra dairesine itiraz edebilir. Bu süre hak düşürücüdür; kaçırılırsa takip kesinleşir.</p>

          <h2>İtiraz nereye, nasıl yapılır?</h2>
          <p>İtiraz, takibin yapıldığı <strong>icra müdürlüğüne</strong> yazılı ya da sözlü olarak bildirilir. İtiraz dilekçesinde borca mı, imzaya mı yoksa yetkiye mi itiraz edildiği açıkça belirtilmelidir:</p>
          <ul>
            <li><strong>Borca itiraz:</strong> Borcun hiç doğmadığı, ödendiği veya zamanaşımına uğradığı ileri sürülür.</li>
            <li><strong>İmzaya itiraz:</strong> Senetteki imzanın borçluya ait olmadığı iddia ediliyorsa <strong>ayrıca ve açıkça</strong> belirtilmelidir; aksi hâlde imza kabul edilmiş sayılır.</li>
            <li><strong>Yetkiye itiraz:</strong> İcra dairesinin yetkisiz olduğu ileri sürülür.</li>
          </ul>

          <h2>İtirazın sonucu</h2>
          <p>Süresinde yapılan itiraz, takibi <strong>kendiliğinden durdurur</strong>. Bu durumda takibe devam edebilmek için alacaklının mahkemeye başvurması gerekir.</p>

          <h2>Alacaklının başvurabileceği yollar</h2>
          <ul>
            <li><strong>İtirazın kaldırılması:</strong> Alacaklının elinde İİK m. 68 anlamında belge (imzası ikrar edilmiş senet, resmî belge vb.) varsa, itirazın tebliğinden itibaren <strong>6 ay</strong> içinde icra mahkemesine başvurur.</li>
            <li><strong>İtirazın iptali:</strong> Elinde bu nitelikte belge yoksa, itirazın tebliğinden itibaren <strong>1 yıl</strong> içinde genel mahkemede itirazın iptali davası açar.</li>
          </ul>

          <h2>Kötü niyet ve icra inkâr tazminatı</h2>
          <p>İtirazında veya takibinde haksız çıkan taraf aleyhine, şartları varsa alacağın <strong>%20'sinden az olmamak üzere</strong> icra inkâr tazminatına hükmedilebilir. Bu nedenle itirazın da, takibin de dayanağının iyi değerlendirilmesi önemlidir.</p>
""",
  },
  # ------------------------------------------------------------------ GAYRİMENKUL
  {
    "slug": "ortakligin-giderilmesi-davasi.html",
    "cat": "Gayrimenkul Hukuku", "tarih": "2026-11-17", "read": "5 dk okuma",
    "title": "Ortaklığın Giderilmesi (İzale-i Şuyu) Davası | Gelegen Hukuk Bürosu",
    "desc": "Hisseli taşınmazlarda ortaklığın giderilmesi davası: arabuluculuk şartı, aynen taksim, satış yoluyla paylaştırma, masraflar ve süreç. Malatya Gelegen Hukuk Bürosu bilgilendirme yazısı.",
    "h1": "Ortaklığın Giderilmesi (İzale-i Şuyu) Davası",
    "lead": "Miras yoluyla veya birlikte satın alınan hisseli taşınmazlarda paydaşlar anlaşamadığında, ortaklık mahkeme kararıyla sona erdirilebilir. Bu yazıda ortaklığın giderilmesi davasının şartlarını ve işleyişini özetliyoruz.",
    "body": """
          <h2>Ortaklığın giderilmesi nedir?</h2>
          <p>Paylı veya elbirliği mülkiyetine konu bir taşınmazın paydaşlarından her biri, kural olarak ortaklığın giderilmesini isteyebilir (TMK m. 698, 699). Paydaşlar paylaşma biçimi üzerinde anlaşamazsa, ortaklık <strong>sulh hukuk mahkemesinde</strong> açılacak dava ile giderilir.</p>

          <h2>Dava öncesi zorunlu arabuluculuk</h2>
          <p>1 Eylül 2023 tarihinden itibaren taşınmazların ortaklığının giderilmesine ilişkin uyuşmazlıklarda dava açmadan önce <strong>arabulucuya başvurmak dava şartıdır</strong>. Arabuluculukta tüm paydaşlar anlaşırsa taşınmaz, anlaşmaya uygun şekilde paylaştırılır ya da satılır.</p>

          <h2>Davada kimler yer alır?</h2>
          <p>Ortaklığın giderilmesi davasında tapuda kayıtlı <strong>tüm paydaşların</strong> davada yer alması gerekir. Paydaşlardan biri vefat etmişse onun yerine mirasçıları davaya dahil edilir. Bu nedenle davadan önce güncel tapu kaydı ve gerekiyorsa mirasçılık belgesi temin edilmelidir.</p>

          <h2>Mahkeme nasıl paylaştırır?</h2>
          <ol>
            <li><strong>Aynen taksim:</strong> Taşınmaz, değerinde önemli bir azalma olmadan bölünebiliyorsa paydaşlara payları oranında ayrı ayrı bölümler verilir. Gerekirse eşitlik için para ödenmesine karar verilir.</li>
            <li><strong>Satış yoluyla paylaştırma:</strong> Aynen taksim mümkün değilse ya da imar mevzuatı buna izin vermiyorsa taşınmazın <strong>açık artırmayla</strong> satılmasına ve bedelin paylar oranında dağıtılmasına karar verilir. Paydaşların hepsi kabul ederse satış yalnızca paydaşlar arasında yapılabilir.</li>
          </ol>

          <h2>Masraflar kime ait?</h2>
          <p>Ortaklığın giderilmesi davalarında harç ve yargılama giderleri, kural olarak paydaşların <strong>payları oranında</strong> üstlenilir. Davanın başında masraflar davacı tarafından yatırılır; karar sonucunda diğer paydaşlardan payları oranında tahsil edilir.</p>

          <h2>Dikkat edilmesi gerekenler</h2>
          <ul>
            <li>Taşınmaz üzerindeki ipotek ve hacizler, satış sonrasında bedele yansır.</li>
            <li>Taşınmazı kullanan paydaştan, diğer paydaşlar koşulları varsa <strong>ecrimisil</strong> (haksız kullanım tazminatı) talep edebilir.</li>
            <li>Satış öncesinde paydaşların kendi aralarında anlaşması, açık artırmaya göre genellikle daha avantajlıdır.</li>
          </ul>
""",
  },
  {
    "slug": "kira-tespit-ve-tahliye-davasi.html",
    "cat": "Gayrimenkul Hukuku", "tarih": "2026-11-17", "read": "6 dk okuma",
    "title": "Kira Tespit ve Tahliye Davası | Gelegen Hukuk Bürosu",
    "desc": "Kira bedelinin tespiti davası, 5 yıl kuralı, tahliye sebepleri, tahliye taahhüdü, iki haklı ihtar ve kira davalarında arabuluculuk. Malatya Gelegen Hukuk Bürosu bilgilendirme yazısı.",
    "h1": "Kira Tespit ve Tahliye Davası",
    "lead": "Kira ilişkisinde en sık yaşanan iki uyuşmazlık, kira bedelinin belirlenmesi ve kiracının tahliyesidir. Bu yazıda kira tespit davasını ve kanunda sayılan tahliye sebeplerini özetliyoruz.",
    "body": """
          <h2>Kira davalarında önce arabuluculuk</h2>
          <p>1 Eylül 2023 tarihinden itibaren kira ilişkisinden doğan uyuşmazlıklarda dava açmadan önce <strong>arabulucuya başvurmak zorunludur</strong>. İcra ve İflas Kanunu kapsamında icra yoluyla yapılan tahliye talepleri bu zorunluluğun dışındadır. Kira davalarında görevli mahkeme <strong>sulh hukuk mahkemesidir</strong>.</p>

          <h2>Kira tespit davası</h2>
          <p>Kira bedelinin günün koşullarına uygun olarak belirlenmesi için kira tespit davası açılabilir (TBK m. 344):</p>
          <ul>
            <li><strong>İlk beş yıl:</strong> Konut ve çatılı işyeri kiralarında kira artışı, bir önceki kira yılındaki <strong>TÜFE'nin on iki aylık ortalamasını</strong> geçemez.</li>
            <li><strong>Beş yıldan sonra:</strong> Beş yıldan uzun süreli veya beş yıldan sonra yenilenen kira sözleşmelerinde yeni kira bedeli; TÜFE oranı, kiralananın durumu ve <strong>emsal kira bedelleri</strong> dikkate alınarak hâkim tarafından hakkaniyete göre belirlenir.</li>
          </ul>
          <p>Kira tespit davası yeni kira döneminin başlangıcından en geç <strong>otuz gün önce</strong> açılırsa veya kiraya veren bu süre içinde kiracıya yazılı bildirimde bulunursa, belirlenen kira bedeli yeni dönemin başından itibaren geçerli olur (TBK m. 345).</p>

          <h2>Tahliye sebepleri</h2>
          <h3>Kiraya verenden kaynaklanan sebepler</h3>
          <ul>
            <li><strong>İhtiyaç:</strong> Kiraya verenin kendisi, eşi, altsoyu, üstsoyu veya bakmakla yükümlü olduğu kişiler için konut veya işyeri ihtiyacı (TBK m. 350).</li>
            <li><strong>Yeniden inşa ve imar:</strong> Kiralananın esaslı onarımı veya yeniden inşası nedeniyle kullanılmasının imkânsız olması.</li>
            <li><strong>Yeni malikin ihtiyacı:</strong> Kiralananı sonradan edinen kişinin ihtiyacı (TBK m. 351).</li>
          </ul>
          <h3>Kiracıdan kaynaklanan sebepler</h3>
          <ul>
            <li><strong>Yazılı tahliye taahhüdü:</strong> Kiracının, kiralananın tesliminden sonra verdiği geçerli yazılı taahhüt (TBK m. 352/1).</li>
            <li><strong>İki haklı ihtar:</strong> Bir kira yılı içinde kira bedelinin ödenmemesi nedeniyle iki haklı ihtara sebep olunması (TBK m. 352/2).</li>
            <li><strong>Ödeme temerrüdü:</strong> Kira bedelinin ödenmemesi hâlinde verilen süreye rağmen ödeme yapılmaması.</li>
          </ul>
          <p>Her tahliye sebebinin kendine özgü dava açma süresi vardır; örneğin ihtiyaç nedeniyle tahliye davası, belirli süreli sözleşmenin bitiminden itibaren <strong>bir ay</strong> içinde açılmalıdır.</p>

          <h2>On yıllık uzama süresi</h2>
          <p>Konut ve çatılı işyeri kiralarında, on yıllık uzama süresinin sonunda kiraya veren, bu süreyi izleyen her uzama yılının bitiminden en az üç ay önce bildirimde bulunmak kaydıyla sözleşmeyi herhangi bir sebep göstermeksizin sona erdirebilir (TBK m. 347).</p>
""",
  },
  # ------------------------------------------------------------------ MİRAS
  {
    "slug": "mirasin-reddi-ve-mirascilik-belgesi.html",
    "cat": "Miras Hukuku", "tarih": "2026-11-17", "read": "5 dk okuma",
    "title": "Mirasın Reddi ve Mirasçılık Belgesi | Gelegen Hukuk Bürosu",
    "desc": "Mirasçılık belgesi (veraset ilamı) nereden alınır, mirasın reddi süresi (3 ay), borca batık terekenin hükmen reddi. Malatya Gelegen Hukuk Bürosu bilgilendirme yazısı.",
    "h1": "Mirasın Reddi ve Mirasçılık Belgesi",
    "lead": "Bir yakının vefatından sonra mirasçıların ilk yapması gerekenler, mirasçılık belgesinin alınması ve terekenin borçlu olup olmadığının araştırılmasıdır. Bu yazıda mirasçılık belgesini ve mirasın reddini özetliyoruz.",
    "body": """
          <h2>Mirasçılık belgesi (veraset ilamı) nedir?</h2>
          <p>Mirasçılık belgesi, kimlerin mirasçı olduğunu ve miras paylarını gösteren resmî belgedir (TMK m. 598). Bankadaki hesapların çekilmesi, tapuda intikal işlemleri ve araç devri gibi işlemler için bu belge gerekir.</p>
          <ul>
            <li><strong>Noterden:</strong> Mirasçılardan biri, kimlik belgesiyle herhangi bir notere başvurarak mirasçılık belgesi alabilir.</li>
            <li><strong>Sulh hukuk mahkemesinden:</strong> Yabancılık unsuru bulunan veya noterlikçe düzenlenemeyen durumlarda mahkemeye başvurulur.</li>
          </ul>

          <h2>Mirasın reddi nedir?</h2>
          <p>Yasal ve atanmış mirasçılar mirası reddedebilir (TMK m. 605). Mirası reddeden kişi mirasçılık sıfatını kaybeder; böylece terekenin borçlarından da sorumlu olmaz. Ret, özellikle <strong>borçları mal varlığından fazla</strong> olan terekelerde başvurulan bir yoldur.</p>

          <h2>Mirasın reddi süresi: 3 ay</h2>
          <p>Ret süresi <strong>üç aydır</strong> (TMK m. 606). Bu süre:</p>
          <ul>
            <li>Yasal mirasçılar için, mirasçı olduklarını daha sonra öğrendikleri ispat edilmedikçe <strong>miras bırakanın ölümünü öğrendikleri tarihten</strong>,</li>
            <li>Vasiyetnameyle atanmış mirasçılar için, tasarrufun kendilerine resmen bildirildiği tarihten başlar.</li>
          </ul>
          <p>Ret beyanı, miras bırakanın son yerleşim yeri <strong>sulh hukuk mahkemesine</strong> sözlü veya yazılı olarak yapılır. Ret kayıtsız ve şartsız olmalıdır.</p>

          <h2>Mirası kabul sayılan davranışlar</h2>
          <p>Ret süresi içinde terekeye ilişkin olağan yönetim işleri dışındaki işlemleri yapan, tereke mallarını gizleyen veya kendine mal eden mirasçı mirası reddedemez (TMK m. 610). Örneğin miras bırakanın aracını satmak veya banka hesabındaki parayı kendi ihtiyaçları için kullanmak, mirasın kabulü anlamına gelebilir.</p>

          <h2>Borca batık terekenin hükmen reddi</h2>
          <p>Ölüm tarihinde miras bırakanın <strong>ödemeden aczi açıkça belli</strong> veya resmen tespit edilmişse miras reddedilmiş sayılır (TMK m. 605/2). Bu durumda üç aylık süreye bağlı olmaksızın mahkemeden <strong>terekenin borca batık olduğunun tespiti</strong> istenebilir. Ancak mirasçının terekeyi sahiplenen davranışları bu imkânı ortadan kaldırabilir.</p>

          <h2>Reddin sonuçları</h2>
          <p>Mirası reddeden mirasçının payı, miras bırakan ondan önce ölmüş gibi onun altsoyuna geçer. Bu nedenle borçlu terekelerde, aynı riskle karşılaşmamaları için mirası reddeden kişinin çocuklarının da ret beyanında bulunması gerekebilir.</p>
""",
  },
  # ------------------------------------------------------------------ CEZA
  {
    "slug": "hagb-nedir.html",
    "cat": "Ceza Hukuku", "tarih": "2026-11-17", "read": "5 dk okuma",
    "title": "HAGB Nedir? Hükmün Açıklanmasının Geri Bırakılması | Gelegen Hukuk Bürosu",
    "desc": "Hükmün açıklanmasının geri bırakılması (HAGB) şartları, 5 yıllık denetim süresi, adli sicile etkisi ve HAGB kararına itiraz (CMK 231). Malatya Gelegen Hukuk Bürosu bilgilendirme yazısı.",
    "h1": "HAGB Nedir? Hükmün Açıklanmasının Geri Bırakılması",
    "lead": "Hükmün açıklanmasının geri bırakılması (HAGB), belirli şartlar altında sanık hakkında kurulan hükmün sonuç doğurmamasını sağlayan bir kurumdur. Bu yazıda HAGB'nin şartlarını ve sonuçlarını özetliyoruz.",
    "body": """
          <h2>HAGB nedir?</h2>
          <p>Ceza Muhakemesi Kanunu (CMK) m. 231 uyarınca mahkeme, sanık hakkında mahkûmiyet hükmü kurduktan sonra bu hükmün <strong>açıklanmasını geri bırakabilir</strong>. Bu durumda hüküm, belirlenen denetim süresi boyunca sanık hakkında hukuki sonuç doğurmaz.</p>

          <h2>HAGB'nin şartları</h2>
          <ul>
            <li>Sanığa yüklenen suçtan dolayı verilen cezanın <strong>iki yıl veya daha az</strong> süreli hapis veya adli para cezası olması,</li>
            <li>Sanığın daha önce <strong>kasıtlı bir suçtan mahkûm olmamış</strong> olması,</li>
            <li>Mahkemece, sanığın kişilik özellikleri ve duruşmadaki tutum ve davranışları göz önünde bulundurularak <strong>yeniden suç işlemeyeceği kanaatine</strong> varılması,</li>
            <li>Suçun işlenmesiyle mağdurun veya kamunun uğradığı <strong>zararın</strong> aynen iade, eski hâle getirme veya tazmin suretiyle tamamen giderilmesi,</li>
            <li>Sanığın HAGB'yi <strong>kabul etmesi</strong> — sanık kabul etmezse bu karar verilemez.</li>
          </ul>

          <h2>Denetim süresi</h2>
          <p>HAGB kararı verildiğinde sanık <strong>beş yıllık denetim süresine</strong> tabi tutulur. Mahkeme, bu süre içinde sanığın denetimli serbestlik tedbiri olarak bir yıldan fazla olmamak üzere belirli yükümlülüklere uymasına da karar verebilir.</p>
          <ul>
            <li>Denetim süresi içinde <strong>kasıtlı yeni bir suç işlenmez</strong> ve yükümlülüklere uyulursa, açıklanması geri bırakılan hüküm ortadan kaldırılır ve <strong>dava düşer</strong>.</li>
            <li>Denetim süresi içinde kasıtlı yeni bir suç işlenirse, mahkeme <strong>hükmü açıklar</strong> ve ceza uygulanır.</li>
          </ul>

          <h2>HAGB adli sicil kaydında görünür mü?</h2>
          <p>HAGB kararları adli sicil kaydında yer almaz; bu kararlar yalnızca kanunda belirtilen amaçla kullanılmak üzere ayrı bir sisteme kaydedilir. Bu kayıt, ancak yeni bir soruşturma veya kovuşturma nedeniyle savcılık, hâkim veya mahkeme tarafından istenmesi hâlinde görülebilir.</p>

          <h2>HAGB kararına itiraz</h2>
          <p>HAGB kararına karşı istinaf veya temyiz yoluna değil, <strong>itiraz</strong> yoluna başvurulur (CMK m. 231/12). İtiraz, kararın öğrenilmesinden itibaren kanunda öngörülen süre içinde yapılmalıdır. Sanık, beraat etmesi gerektiğini düşünüyorsa HAGB'yi kabul edip etmeme konusunda dikkatli bir değerlendirme yapmalıdır.</p>
""",
  },
  # ------------------------------------------------------------------ İDARE
  {
    "slug": "idari-para-cezasina-itiraz.html",
    "cat": "İdare Hukuku", "tarih": "2026-11-17", "read": "4 dk okuma",
    "title": "İdari Para Cezasına ve Trafik Cezasına İtiraz | Gelegen Hukuk Bürosu",
    "desc": "İdari para cezalarına ve trafik cezalarına itiraz süresi (15 gün), başvuru yeri, erken ödeme indirimi ve itiraz süreci. Malatya Gelegen Hukuk Bürosu bilgilendirme yazısı.",
    "h1": "İdari Para Cezasına ve Trafik Cezasına İtiraz",
    "lead": "Trafik cezası, belediye zabıta cezası veya diğer idari para cezalarına karşı itiraz hakkı, kısa bir süreye bağlıdır. Bu yazıda itirazın nereye ve ne zaman yapılacağını özetliyoruz.",
    "body": """
          <h2>İtiraz süresi: 15 gün</h2>
          <p>Kabahatler Kanunu m. 27 uyarınca idari para cezası kararına karşı, kararın <strong>tebliğinden veya öğrenilmesinden itibaren 15 gün</strong> içinde başvurulabilir. Bu süre geçtikten sonra karar kesinleşir.</p>

          <h2>İtiraz nereye yapılır?</h2>
          <ul>
            <li><strong>Kural olarak sulh ceza hâkimliği:</strong> Trafik cezaları, zabıta cezaları ve Kabahatler Kanunu kapsamındaki pek çok idari para cezasına karşı başvuru yeri sulh ceza hâkimliğidir.</li>
            <li><strong>İdare mahkemesi:</strong> Bazı özel kanunlarda (ör. imar, çevre, rekabet, vergi mevzuatı) idari yaptırımlara karşı idare veya vergi mahkemesine başvurulması öngörülmüştür. Bu durumda dava açma süresi de farklıdır.</li>
          </ul>
          <p>Cezanın hangi kanuna dayandığı, karar tutanağında yer alır. Başvuru yerini doğru belirlemek için tutanağın dikkatle incelenmesi gerekir.</p>

          <h2>Erken ödeme indirimi itiraz hakkını kaldırır mı?</h2>
          <p>İdari para cezası, tebliğden itibaren 15 gün içinde ödenirse dörtte bir oranında indirim uygulanır (Kabahatler Kanunu m. 17/6). Cezanın indirimli olarak ödenmesi <strong>itiraz hakkını ortadan kaldırmaz</strong>; itiraz kabul edilirse ödenen tutar iade edilir.</p>

          <h2>İtiraz dilekçesinde neler yer almalı?</h2>
          <ul>
            <li>Başvuranın kimlik ve adres bilgileri,</li>
            <li>İtiraz edilen kararın tarihi, sayısı ve tebliğ tarihi,</li>
            <li>Cezanın neden hukuka aykırı olduğuna ilişkin açıklamalar,</li>
            <li>Varsa deliller (fotoğraf, video, tanık bilgileri, belgeler).</li>
          </ul>

          <h2>İtirazın sonucu</h2>
          <p>Sulh ceza hâkimliği başvuruyu kural olarak dosya üzerinden inceler; gerekli görürse ilgilileri dinleyebilir. Hâkimlik cezayı kaldırabilir veya başvuruyu reddedebilir. Bu karara karşı da Ceza Muhakemesi Kanunu hükümlerine göre itiraz yoluna gidilebilir.</p>
""",
  },
]
