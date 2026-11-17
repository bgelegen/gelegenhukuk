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
    "desc": "Çekişmeli boşanma davasının sebepleri (TMK 161-166), hak düşürücü süreler, deliller, tanıklar ve yargılama süreci. Gelegen Hukuk, Malatya.",
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
    "desc": "Tedbir, iştirak, yoksulluk ve yardım nafakası nedir, kimler talep edebilir, nafaka nasıl artırılır veya kaldırılır? Gelegen Hukuk, Malatya.",
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
    "desc": "Boşanmada velayetin belirlenmesi, çocuğun üstün yararı, sosyal inceleme raporu, ortak velayet ve velayetin değiştirilmesi davası. Gelegen Hukuk, Malatya.",
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
    "desc": "İşe iade davasının şartları, 30 iş günü ve 1 aylık başvuru süreleri, zorunlu arabuluculuk ve işe başlatmama tazminatı. Gelegen Hukuk, Malatya.",
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
    "desc": "Kıdem tazminatına hak kazanma şartları, istifa eden işçinin durumu, hesaplama yöntemi, tavan, zamanaşımı ve arabuluculuk. Gelegen Hukuk, Malatya.",
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
    "desc": "Hisseli taşınmazlarda ortaklığın giderilmesi davası: arabuluculuk şartı, aynen taksim, satış yoluyla paylaştırma, masraflar ve süreç. Gelegen Hukuk, Malatya.",
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
    "desc": "Kira bedelinin tespiti davası, 5 yıl kuralı, tahliye sebepleri, tahliye taahhüdü, iki haklı ihtar ve kira davalarında arabuluculuk. Gelegen Hukuk, Malatya.",
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
    "desc": "Mirasçılık belgesi (veraset ilamı) nereden alınır, mirasın reddi süresi (3 ay), borca batık terekenin hükmen reddi. Gelegen Hukuk, Malatya.",
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
    "desc": "Hükmün açıklanmasının geri bırakılması (HAGB) şartları, 5 yıllık denetim süresi, adli sicile etkisi ve HAGB kararına itiraz (CMK 231). Gelegen Hukuk, Malatya.",
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
    "desc": "İdari para cezalarına ve trafik cezalarına itiraz süresi (15 gün), başvuru yeri, erken ödeme indirimi ve itiraz süreci. Gelegen Hukuk, Malatya.",
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

# =====================================================================
#  2. PARTİ — yüksek arama hacimli konular (17 Kasım 2026)
# =====================================================================
MAKALELER += [
  # ------------------------------------------------------------------ AİLE
  {
    "slug": "bosanma-davasi-ne-kadar-surer.html",
    "cat": "Aile Hukuku", "tarih": "2026-11-17", "read": "5 dk okuma",
    "title": "Boşanma Davası Ne Kadar Sürer? | Gelegen Hukuk Bürosu",
    "desc": "Anlaşmalı ve çekişmeli boşanma davası ne kadar sürer, süreyi uzatan etkenler nelerdir, istinaf ve temyiz süreleri. Gelegen Hukuk, Malatya.",
    "h1": "Boşanma Davası Ne Kadar Sürer?",
    "lead": "Boşanma davasının süresi, davanın anlaşmalı mı çekişmeli mi olduğuna, delil durumuna ve mahkemenin iş yüküne göre büyük farklılık gösterir. Bu yazıda sürecin aşamalarını ve süreyi etkileyen etkenleri özetliyoruz.",
    "body": """
          <h2>Anlaşmalı boşanma</h2>
          <p><a href="anlasmali-bosanma-nasil-yapilir.html">Anlaşmalı boşanmada</a> taraflar tüm konularda uzlaştığı için dava genellikle <strong>tek duruşmada</strong> sonuçlanır. Süreyi belirleyen başlıca etken, mahkemenin duruşma gününü ne zamana verdiğidir. Karar açıklandıktan sonra gerekçeli kararın yazılması, tebliği ve kesinleşmesiyle süreç tamamlanır. Taraflar kanun yoluna başvurmayacaklarını duruşmada beyan ederse kesinleşme hızlanabilir.</p>

          <h2>Çekişmeli boşanma</h2>
          <p><a href="cekismeli-bosanma-davasi.html">Çekişmeli boşanma</a> davaları, ilk derece mahkemesinde çoğunlukla <strong>aylar</strong>, kanun yollarıyla birlikte ise <strong>yıllar</strong> sürebilir. Dava şu aşamalardan geçer:</p>
          <ol>
            <li><strong>Dilekçeler aşaması:</strong> Dava, cevap, cevaba cevap ve ikinci cevap dilekçeleri. Her dilekçe için kural olarak iki haftalık süre vardır.</li>
            <li><strong>Ön inceleme duruşması:</strong> Uyuşmazlık konuları ve deliller belirlenir.</li>
            <li><strong>Tahkikat:</strong> Tanıklar dinlenir, kurum yazışmaları yapılır; çocuk varsa sosyal inceleme raporu alınır.</li>
            <li><strong>Karar duruşması:</strong> Boşanma, velayet, nafaka ve tazminat hakkında hüküm kurulur.</li>
            <li><strong>İstinaf ve temyiz:</strong> Kararın tebliğinden itibaren <strong>iki hafta</strong> içinde istinafa, istinaf kararına karşı yine iki hafta içinde temyize başvurulabilir.</li>
          </ol>

          <h2>Süreyi uzatan etkenler</h2>
          <ul>
            <li>Tarafların adreslerinin bilinmemesi veya yurt dışında olması nedeniyle tebligatın gecikmesi,</li>
            <li>Çok sayıda tanığın dinlenmesi veya tanıkların başka şehirlerde olması (talimat yoluyla dinleme),</li>
            <li>Sosyal inceleme raporu, bilirkişi incelemesi veya kurum yazışmalarının beklenmesi,</li>
            <li>Mal rejimi tasfiyesi gibi taleplerin aynı dosyada ileri sürülmesi,</li>
            <li>Kararın istinaf ve temyiz aşamalarından geçmesi.</li>
          </ul>

          <h2>Süreç nasıl kısaltılabilir?</h2>
          <ul>
            <li>Delillerin ve tanık listesinin dilekçelerle birlikte eksiksiz sunulması,</li>
            <li>Tarafların güncel adres bilgilerinin doğru bildirilmesi,</li>
            <li>Çekişmeli dava devam ederken taraflar anlaşırsa, şartları varsa davanın <strong>anlaşmalı boşanmaya dönüştürülmesi</strong>,</li>
            <li>Taraflar karardan memnunsa kanun yoluna başvurmaktan feragat edilmesi.</li>
          </ul>

          <h2>Karar kesinleşmeden yeniden evlenilebilir mi?</h2>
          <p>Hayır. Boşanma kararı kesinleşmeden taraflar yeniden evlenemez. Ayrıca kadın için, evliliğin sona ermesinden itibaren <strong>300 günlük bekleme süresi</strong> vardır (TMK m. 132); bu süre doğumla sona erer ve gebe olmadığının tıbbi raporla belgelenmesi hâlinde mahkemece kaldırılabilir.</p>
""",
  },
  {
    "slug": "bosanmada-mal-paylasimi.html",
    "cat": "Aile Hukuku", "tarih": "2026-11-17", "read": "6 dk okuma",
    "title": "Boşanmada Mal Paylaşımı Nasıl Yapılır? | Gelegen Hukuk Bürosu",
    "desc": "Edinilmiş mallara katılma rejimi, kişisel mallar, katılma alacağı, 2002 öncesi mallar, zamanaşımı ve mal paylaşımı davası. Gelegen Hukuk, Malatya.",
    "h1": "Boşanmada Mal Paylaşımı Nasıl Yapılır?",
    "lead": "Boşanmada en çok merak edilen konulardan biri, evlilik süresince edinilen malların nasıl paylaşılacağıdır. Türk hukukunda paylaşım, eşlerin tabi olduğu mal rejimine göre yapılır. Bu yazıda temel kuralları özetliyoruz.",
    "body": """
          <h2>Yasal mal rejimi: edinilmiş mallara katılma</h2>
          <p>Eşler evlenmeden önce veya evlilik sırasında noterde başka bir mal rejimi seçmemişse, 1 Ocak 2002 tarihinden itibaren <strong>edinilmiş mallara katılma rejimi</strong> uygulanır (TMK m. 202). Bu rejimde her eşin malları ikiye ayrılır: <strong>edinilmiş mallar</strong> ve <strong>kişisel mallar</strong>.</p>

          <h2>Edinilmiş mallar</h2>
          <p>Bir eşin evlilik süresince <strong>karşılığını vererek</strong> elde ettiği malvarlığı değerleridir (TMK m. 219). Başlıcaları:</p>
          <ul>
            <li>Çalışmasının karşılığı olan edinimler (maaş, kazanç ve bunlarla alınan mallar),</li>
            <li>Sosyal güvenlik ve sosyal yardım kurumlarının yaptığı ödemeler,</li>
            <li>Kişisel malların gelirleri (ör. evlilik öncesi alınmış bir evin kira geliri),</li>
            <li>Edinilmiş malların yerine geçen değerler.</li>
          </ul>

          <h2>Kişisel mallar (paylaşıma girmez)</h2>
          <ul>
            <li>Eşlerden birinin yalnızca kişisel kullanımına yarayan eşyalar,</li>
            <li>Mal rejiminin başlangıcında, yani <strong>evlilikten önce</strong> sahip olunan mallar,</li>
            <li>Evlilik sırasında <strong>miras veya bağış</strong> gibi karşılıksız kazanma yoluyla edinilen mallar,</li>
            <li>Manevi tazminat alacakları ve kişisel malların yerine geçen değerler (TMK m. 220).</li>
          </ul>

          <h2>Katılma alacağı nasıl hesaplanır?</h2>
          <p>Her eşin edinilmiş mallarının toplam değerinden, bu mallara ilişkin borçlar düşülür; kalan miktar <strong>artık değerdir</strong>. Her eş, diğer eşin artık değerinin <strong>yarısı</strong> üzerinde hak sahibidir (TMK m. 236). Karşılıklı alacaklar takas edilerek ödenecek tutar bulunur. Mallar, tasfiye anındaki (karara en yakın tarihteki) <strong>sürüm değerleriyle</strong> hesaba katılır.</p>
          <p>Örneğin evlilik içinde bir eşin maaşıyla kendi adına alınan daire, kural olarak edinilmiş maldır ve diğer eş bu dairenin değerinin yarısı oranında katılma alacağı isteyebilir. Kredi borcu varsa önce borç düşülür.</p>

          <h2>2002 öncesi edinilen mallar</h2>
          <p>1 Ocak 2002 öncesinde evli olan eşler için o tarihe kadar <strong>mal ayrılığı rejimi</strong> geçerliydi. Bu dönemde edinilen mallar için katılma alacağı değil, ispat edilebilen katkı oranında <strong>katkı payı alacağı</strong> talep edilebilir. Uzun süreli evliliklerde tasfiye, iki dönem için ayrı ayrı yapılır.</p>

          <h2>Mal rejimi ne zaman sona erer?</h2>
          <p>Boşanma hâlinde mal rejimi, <strong>boşanma davasının açıldığı tarihte</strong> sona erer (TMK m. 225). Bu tarihten sonra edinilen mallar paylaşıma girmez.</p>

          <h2>Mal paylaşımı davası</h2>
          <ul>
            <li><strong>Görevli mahkeme:</strong> Aile mahkemesi.</li>
            <li><strong>Zaman:</strong> Boşanma davasıyla birlikte veya boşanma kararı kesinleştikten sonra ayrı bir davayla açılabilir. Uygulamada mal rejimi davası, boşanma davasının sonucunun beklenmesi nedeniyle çoğunlukla bekletilir.</li>
            <li><strong>Zamanaşımı:</strong> Yargıtay uygulamasına göre boşanma kararının kesinleşmesinden itibaren <strong>on yıl</strong>.</li>
            <li><strong>İhtiyati tedbir:</strong> Dava sırasında malın elden çıkarılması riskine karşı tapu kaydına tedbir şerhi konulması istenebilir.</li>
          </ul>
""",
  },
  # ------------------------------------------------------------------ CEZA
  {
    "slug": "gozalti-suresi-ve-supheli-haklari.html",
    "cat": "Ceza Hukuku", "tarih": "2026-11-17", "read": "5 dk okuma",
    "title": "Gözaltı Süresi Ne Kadar? Şüpheli Hakları | Gelegen Hukuk Bürosu",
    "desc": "Gözaltı süresi (24 saat, toplu suçlarda 4 gün), gözaltına itiraz, şüphelinin susma ve avukat hakkı, yakınlara haber verilmesi ve tutuklama. Gelegen Hukuk, Malatya.",
    "h1": "Gözaltı Süresi Ne Kadar? Şüphelinin Hakları",
    "lead": "Bir yakınınızın gözaltına alındığını öğrendiğinizde ilk saatler büyük önem taşır. Bu yazıda gözaltı sürelerini, gözaltındaki kişinin haklarını ve gözaltına itiraz yolunu özetliyoruz.",
    "body": """
          <h2>Gözaltı süresi</h2>
          <p>Ceza Muhakemesi Kanunu (CMK) m. 91 uyarınca gözaltı süresi, yakalama yerine en yakın hâkim veya mahkemeye gönderilmesi için zorunlu süre hariç, yakalama anından itibaren <strong>24 saati</strong> geçemez.</p>
          <ul>
            <li><strong>Toplu suçlarda:</strong> Cumhuriyet savcısı, her defasında bir günü geçmemek üzere üç gün süreyle uzatma kararı verebilir. Böylece toplu suçlarda gözaltı süresi en fazla <strong>dört güne</strong> çıkabilir.</li>
            <li>Terör suçları gibi özel düzenlemeler bulunan suçlarda farklı süreler uygulanabilir.</li>
          </ul>
          <p>Süre sonunda şüpheli ya serbest bırakılır ya da Cumhuriyet savcılığına çıkarılır; savcılık gerekli görürse tutuklama veya adli kontrol talebiyle sulh ceza hâkimliğine sevk eder.</p>

          <h2>Gözaltındaki kişinin hakları</h2>
          <ul>
            <li><strong>Suçlamayı öğrenme:</strong> Kendisine yöneltilen suçlamanın ne olduğu bildirilir (CMK m. 147).</li>
            <li><strong>Susma hakkı:</strong> Şüpheli, yüklenen suç hakkında açıklamada bulunmama hakkına sahiptir.</li>
            <li><strong>Avukat (müdafi) hakkı:</strong> Gözaltının her aşamasında avukatla görüşebilir; avukatı ifade sırasında hazır bulunabilir. Kanunda sayılan hâllerde baro tarafından zorunlu müdafi atanır.</li>
            <li><strong>Yakınlarına haber verilmesi:</strong> Yakalanan ve gözaltı süresi uzatılan kişinin durumu, şüphelinin seçeceği bir yakınına veya belirleyeceği bir kişiye gecikmeksizin bildirilir (CMK m. 95).</li>
            <li><strong>Lehine delillerin toplanmasını isteme</strong> ve doktor muayenesi.</li>
          </ul>

          <h2>Gözaltına itiraz</h2>
          <p>Gözaltına alınan kişi, müdafii, yasal temsilcisi, eşi veya birinci ya da ikinci derecede kan hısımı; yakalama veya gözaltı işlemine ya da gözaltı süresinin uzatılmasına karşı, derhal serbest bırakılmayı sağlamak için <strong>sulh ceza hâkimliğine</strong> başvurabilir (CMK m. 91/5). Hâkim incelemeyi evrak üzerinden yaparak en geç <strong>24 saat</strong> içinde karar verir.</p>

          <h2>Kolluk ifadesi ile savcılık ifadesi arasındaki fark</h2>
          <p>Kollukta müdafi hazır bulunmaksızın alınan ifade, şüpheli hâkim veya mahkeme huzurunda doğrulamadıkça hükme esas alınamaz (CMK m. 148/4). Bu nedenle ilk ifadeden itibaren avukat desteği, savunmanın sağlıklı kurulması bakımından önemlidir.</p>

          <h2>Tutuklama ve adli kontrol</h2>
          <p>Savcılığın talebi üzerine sulh ceza hâkimliği; kuvvetli suç şüphesi ve kaçma ya da delilleri karartma şüphesi gibi bir tutuklama nedeni varsa <strong>tutuklama</strong>, aksi hâlde yurt dışına çıkış yasağı, imza yükümlülüğü gibi <strong>adli kontrol</strong> tedbirlerine karar verebilir (CMK m. 100, 109). Tutukluluk hâli soruşturma evresinde en geç 30 günlük süreler içinde incelenir; şüpheli ve müdafii her zaman tahliye talebinde bulunabilir.</p>
""",
  },
  {
    "slug": "tehdit-sucu-ve-cezasi.html",
    "cat": "Ceza Hukuku", "tarih": "2026-11-17", "read": "5 dk okuma",
    "title": "Tehdit Suçu ve Cezası (TCK 106) | Gelegen Hukuk Bürosu",
    "desc": "Tehdit suçu nedir, basit ve nitelikli tehdidin cezası, şikâyet süresi, uzlaştırma ve mesajla tehdit. TCK 106 kapsamında Gelegen Hukuk, Malatya.",
    "h1": "Tehdit Suçu ve Cezası (TCK 106)",
    "lead": "Tehdit, uygulamada en sık karşılaşılan suçlardan biridir ve çoğu zaman mesaj, telefon veya sosyal medya yoluyla işlenir. Bu yazıda tehdit suçunun unsurlarını, cezasını ve yargılama sürecini özetliyoruz.",
    "body": """
          <h2>Tehdit suçu nedir?</h2>
          <p>Türk Ceza Kanunu m. 106 uyarınca tehdit, bir başkasını kendisinin veya yakınının hayatına, vücut veya cinsel dokunulmazlığına ya da malvarlığına yönelik bir saldırı gerçekleştireceğinden bahisle korkutmaktır. Suçun oluşması için tehdidin, mağdurda korku yaratmaya <strong>elverişli</strong> olması yeterlidir; söylenen kötülüğün gerçekten yapılması gerekmez.</p>

          <h2>Basit tehdit</h2>
          <ul>
            <li><strong>Hayata, vücut veya cinsel dokunulmazlığa yönelik tehdit:</strong> Altı aydan iki yıla kadar hapis cezası (TCK m. 106/1, birinci cümle).</li>
            <li><strong>Malvarlığına büyük zarar verileceğinden veya sair bir kötülük edileceğinden bahisle tehdit:</strong> Mağdurun <strong>şikâyeti üzerine</strong>, altı aya kadar hapis veya adli para cezası (TCK m. 106/1, ikinci cümle).</li>
          </ul>

          <h2>Nitelikli tehdit</h2>
          <p>Tehdidin aşağıdaki şekillerde işlenmesi hâlinde ceza <strong>iki yıldan beş yıla kadar</strong> hapistir (TCK m. 106/2):</p>
          <ul>
            <li>Silahla,</li>
            <li>Kişinin kendisini tanınmayacak bir hâle koyması suretiyle, imzasız mektupla veya özel işaretlerle,</li>
            <li>Birden fazla kişi tarafından birlikte,</li>
            <li>Var olan veya var sayılan suç örgütlerinin oluşturdukları korkutucu güçten yararlanılarak.</li>
          </ul>
          <p>Tehdit amacıyla kasten öldürme, yaralama veya mala zarar verme suçları da işlenirse, bu suçlardan ayrıca ceza verilir (TCK m. 106/3).</p>

          <h2>Şikâyet ve uzlaştırma</h2>
          <p>Malvarlığına yönelik veya "sair kötülük" içeren basit tehdit şikâyete bağlıdır; şikâyet, fiilin ve failin öğrenilmesinden itibaren <strong>altı ay</strong> içinde yapılmalıdır (TCK m. 73). Hayata veya vücut dokunulmazlığına yönelik basit tehdit ise şikâyete bağlı değildir, ancak <strong>uzlaştırma</strong> kapsamındadır. Uzlaştırma kapsamındaki suçlarda taraflar uzlaşırsa soruşturma veya kovuşturma sona erer.</p>

          <h2>Mesajla veya sosyal medyadan tehdit</h2>
          <p>Telefon mesajı, e-posta, anlık mesajlaşma uygulamaları veya sosyal medya üzerinden yapılan tehditler de suç oluşturur. Bu durumda:</p>
          <ul>
            <li>Mesajların ekran görüntüleri alınmalı, mümkünse cihaz ve hesap bilgileri korunmalıdır,</li>
            <li>Mesajlar silinmemeli; savcılık gerekirse ilgili kurum ve şirketlerden kayıtları talep edebilir,</li>
            <li>Şikâyet, Cumhuriyet başsavcılığına veya kolluğa yapılabilir.</li>
          </ul>

          <h2>Tehdit mağduru ne yapabilir?</h2>
          <p>Şikâyetin yanı sıra, özellikle aile içinde veya yakın ilişkide yaşanan tehditlerde 6284 sayılı Kanun kapsamında <strong>uzaklaştırma ve koruma kararı</strong> talep edilebilir. Bu kararlar, ceza soruşturmasından bağımsız olarak hızla verilebilir.</p>
""",
  },
  # ------------------------------------------------------------------ İŞ
  {
    "slug": "ihbar-tazminati-ve-ihbar-sureleri.html",
    "cat": "İş Hukuku", "tarih": "2026-11-17", "read": "4 dk okuma",
    "title": "İhbar Tazminatı ve İhbar Süreleri | Gelegen Hukuk Bürosu",
    "desc": "İhbar süreleri (2, 4, 6, 8 hafta), ihbar tazminatına hak kazanma şartları, hesaplama, istifa eden işçinin ihbar yükümlülüğü ve iş arama izni. Gelegen Hukuk, Malatya.",
    "h1": "İhbar Tazminatı ve İhbar Süreleri",
    "lead": "Belirsiz süreli iş sözleşmesini sona erdirmek isteyen taraf, kural olarak karşı tarafa önceden bildirimde bulunmak zorundadır. Bu bildirime uyulmazsa ihbar tazminatı gündeme gelir. Bu yazıda süreleri ve hesaplamayı özetliyoruz.",
    "body": """
          <h2>İhbar (bildirim) süreleri</h2>
          <p>İş Kanunu m. 17 uyarınca belirsiz süreli iş sözleşmeleri, işçinin kıdemine göre aşağıdaki sürelerden önce karşı tarafa bildirilerek feshedilir:</p>
          <ul>
            <li>İşi <strong>6 aydan az</strong> sürmüş işçi için: <strong>2 hafta</strong>,</li>
            <li>İşi <strong>6 ay – 1,5 yıl</strong> sürmüş işçi için: <strong>4 hafta</strong>,</li>
            <li>İşi <strong>1,5 – 3 yıl</strong> sürmüş işçi için: <strong>6 hafta</strong>,</li>
            <li>İşi <strong>3 yıldan fazla</strong> sürmüş işçi için: <strong>8 hafta</strong>.</li>
          </ul>
          <p>Bu süreler asgari sürelerdir; iş sözleşmesiyle artırılabilir.</p>

          <h2>İhbar tazminatı ne zaman ödenir?</h2>
          <p>Bildirim şartına uymadan iş sözleşmesini fesheden taraf, bildirim süresine ait ücret tutarında <strong>ihbar tazminatı</strong> ödemek zorundadır. İşveren, bildirim süresine ait ücreti peşin ödeyerek sözleşmeyi hemen de feshedebilir.</p>
          <p>Kanunda sayılan <strong>haklı nedenlerle</strong> yapılan fesihlerde (İş Kanunu m. 24 ve 25) bildirim süresine uyulması gerekmez; bu nedenle ihbar tazminatı da doğmaz.</p>

          <h2>İstifa eden işçi ihbar tazminatı öder mi?</h2>
          <p>Evet, olabilir. Haklı bir nedeni olmadan istifa eden işçi de bildirim sürelerine uymak zorundadır. Bildirim süresine uymadan işten ayrılan işçi, işverene ihbar tazminatı ödemekle yükümlü olabilir. Uygulamada işveren bu tutarı işçinin alacaklarından mahsup etmek isteyebilir.</p>

          <h2>İhbar tazminatı nasıl hesaplanır?</h2>
          <p>İhbar tazminatı, işçinin <strong>giydirilmiş brüt ücreti</strong> üzerinden, kıdemine karşılık gelen bildirim süresi kadar (2, 4, 6 veya 8 hafta) hesaplanır. Giydirilmiş ücrete düzenli ödenen yol, yemek, ikramiye gibi yan haklar dahildir. Kıdem tazminatından farklı olarak ihbar tazminatından <strong>gelir vergisi ve damga vergisi</strong> kesilir; kıdem tazminatındaki gibi bir tavan uygulanmaz.</p>

          <h2>İş arama izni</h2>
          <p>Bildirim süresi içinde işveren, işçiye yeni bir iş bulması için iş saatleri içinde ve ücret kesintisi yapmadan günde en az <strong>iki saat</strong> iş arama izni vermek zorundadır (İş Kanunu m. 27). İşçi isterse bu izinleri toplu olarak, işten ayrılacağı günden önceki günlere rastlatarak kullanabilir.</p>

          <h2>Zamanaşımı ve arabuluculuk</h2>
          <p>İhbar tazminatı alacağı <strong>beş yıllık</strong> zamanaşımına tabidir. Dava açmadan önce <strong>arabulucuya başvurmak zorunludur</strong>. İhbar tazminatı çoğunlukla <a href="kidem-tazminati-sartlari.html">kıdem tazminatı</a> ile birlikte talep edilir.</p>
""",
  },
  {
    "slug": "fazla-mesai-alacagi.html",
    "cat": "İş Hukuku", "tarih": "2026-11-17", "read": "5 dk okuma",
    "title": "Fazla Mesai Ücreti ve Fazla Mesai Alacağı | Gelegen Hukuk Bürosu",
    "desc": "Fazla mesai nedir, haftalık 45 saat sınırı, %50 zamlı ücret, yıllık 270 saat, serbest zaman, fazla mesainin ispatı ve zamanaşımı. Gelegen Hukuk, Malatya.",
    "h1": "Fazla Mesai Ücreti ve Fazla Mesai Alacağı",
    "lead": "Uzun saatler çalışıp karşılığını alamamak, iş ilişkisinde en sık karşılaşılan uyuşmazlıklardan biridir. Bu yazıda fazla mesainin ne olduğunu, nasıl ücretlendirildiğini ve alacağın nasıl ispat edileceğini özetliyoruz.",
    "body": """
          <h2>Fazla çalışma (fazla mesai) nedir?</h2>
          <p>İş Kanunu m. 41 uyarınca fazla çalışma, kanunda yazılı koşullar çerçevesinde <strong>haftalık 45 saati aşan</strong> çalışmalardır. Haftalık çalışma süresi sözleşmeyle 45 saatin altında belirlenmişse, bu sürenin üzerinde ve 45 saate kadar yapılan çalışmalar <strong>fazla sürelerle çalışma</strong> olarak adlandırılır.</p>

          <h2>Fazla mesai ücreti nasıl hesaplanır?</h2>
          <ul>
            <li><strong>Fazla çalışma:</strong> Her bir saat için normal saat ücretinin <strong>yüzde elli</strong> yükseltilmesiyle ödenir.</li>
            <li><strong>Fazla sürelerle çalışma:</strong> Her bir saat için normal saat ücretinin <strong>yüzde yirmi beş</strong> yükseltilmesiyle ödenir.</li>
          </ul>
          <p>Örneğin saat ücreti 100 TL olan bir işçinin 45 saati aşan her çalışma saati için 150 TL ödenmesi gerekir.</p>

          <h2>Serbest zaman</h2>
          <p>İşçi isterse, fazla çalışma ücreti yerine her bir saat fazla çalışma için <strong>1 saat 30 dakika</strong>, fazla sürelerle çalışma için <strong>1 saat 15 dakika</strong> serbest zaman kullanabilir. Serbest zaman, altı ay içinde, çalışma süreleri içinde ve ücretten kesinti yapılmadan kullandırılır.</p>

          <h2>Fazla çalışmanın sınırları</h2>
          <ul>
            <li>Fazla çalışmanın toplamı bir yılda <strong>270 saatten</strong> fazla olamaz.</li>
            <li>Fazla çalışma için işçinin <strong>onayı</strong> alınmalıdır.</li>
            <li>Gece çalışmaları kural olarak <strong>7,5 saati</strong> geçemez; sağlık kuralları bakımından günde 7,5 saat veya daha az çalışılması gereken işlerde fazla çalışma yaptırılamaz.</li>
            <li>18 yaşını doldurmamış işçilere ve gebe, yeni doğum yapmış veya çocuk emziren işçilere fazla çalışma yaptırılamaz.</li>
          </ul>

          <h2>Fazla mesai nasıl ispat edilir?</h2>
          <p>Fazla mesainin ispat yükü kural olarak <strong>işçidedir</strong>. Başlıca deliller:</p>
          <ul>
            <li>İşyeri giriş-çıkış kayıtları, puantaj ve vardiya çizelgeleri,</li>
            <li>İşyerinde birlikte çalışan <strong>tanıkların</strong> beyanları,</li>
            <li>E-posta, mesaj ve sistem kayıtları,</li>
            <li>Ücret bordroları: İşçinin imzasını taşıyan ve fazla mesai tahakkuku içeren bordrolar, kural olarak o aylar için fazla mesainin ödendiğini gösterir; bu nedenle bordrolara itirazi kayıtla imza atılması önem taşır.</li>
          </ul>
          <p>Yargıtay uygulamasında fazla mesainin tanık beyanlarıyla ispatlandığı durumlarda, hesaplanan alacaktan hakkaniyet gereği belirli bir oranda <strong>indirim</strong> yapılabilmektedir.</p>

          <h2>Zamanaşımı ve arabuluculuk</h2>
          <p>Fazla mesai alacağı <strong>beş yıllık</strong> zamanaşımına tabidir; bu nedenle iş ilişkisi sona erdiğinde son beş yıla ait alacaklar talep edilebilir. Dava açmadan önce <strong>arabulucuya başvurmak zorunludur</strong>.</p>
""",
  },
  # ------------------------------------------------------------------ İCRA
  {
    "slug": "maas-haczi.html",
    "cat": "İcra ve İflas Hukuku", "tarih": "2026-11-17", "read": "5 dk okuma",
    "title": "Maaş Haczi: Maaşın Ne Kadarı Haczedilir? | Gelegen Hukuk Bürosu",
    "desc": "Maaş haczi oranı (dörtte bir), nafaka alacağında maaş haczi, emekli maaşı haczi, birden fazla haciz sırası ve maaş haczine itiraz. Gelegen Hukuk, Malatya.",
    "h1": "Maaş Haczi: Maaşın Ne Kadarı Haczedilir?",
    "lead": "Kesinleşen bir icra takibinde alacaklının en sık başvurduğu yollardan biri, borçlunun maaşına haciz konulmasıdır. Bu yazıda maaşın hangi oranda haczedilebileceğini, emekli maaşının durumunu ve itiraz yollarını özetliyoruz.",
    "body": """
          <h2>Maaşın ne kadarı haczedilebilir?</h2>
          <p>İcra ve İflas Kanunu (İİK) m. 83 uyarınca maaşlar, ücretler ve benzeri gelirler; icra müdürünce borçlu ve ailesinin geçimi için gerekli görülen miktar ayrıldıktan sonra haczedilebilir. Ancak haczedilecek miktar <strong>maaşın dörtte birinden az olamaz</strong>. Uygulamada maaşın genellikle dörtte biri oranında kesinti yapılır.</p>
          <p>Asgari ücret alan işçinin maaşı da aynı kurallar çerçevesinde haczedilebilir.</p>

          <h2>Nafaka alacağında maaş haczi</h2>
          <p>Nafaka alacakları için dörtte bir sınırı uygulanmaz; nafaka miktarı kadar haciz konulabilir. Ayrıca nafaka alacakları, sıra bakımından diğer alacaklardan <strong>önce</strong> gelir.</p>

          <h2>Birden fazla haciz varsa ne olur?</h2>
          <p>Aynı maaşa birden fazla alacaklı tarafından haciz konulmuşsa, hacizler <strong>sıraya girer</strong>. Önce gelen haciz tamamen ödenince sıradaki hacze geçilir. Bu nedenle sonradan gelen alacaklıların tahsilatı uzun sürebilir.</p>

          <h2>Emekli maaşı haczedilebilir mi?</h2>
          <p>Sosyal Güvenlik Kanunu (5510 sayılı Kanun) m. 93 uyarınca emekli maaşları, <strong>nafaka borçları hariç</strong> kural olarak haczedilemez. Borçlunun haciz sırasında açıkça rıza göstermesi hâlinde haciz yapılabileceği kabul edilmektedir; ancak kredi sözleşmesi imzalanırken önceden verilen genel nitelikteki muvafakatler, Yargıtay uygulamasına göre geçerli sayılmamaktadır.</p>

          <h2>Haczedilemeyen gelirler</h2>
          <ul>
            <li>Sosyal yardımlar ve bazı kamu ödemeleri,</li>
            <li>Borçlunun ve ailesinin geçimi için zorunlu eşya ve gelirler (İİK m. 82),</li>
            <li>Kanunla haczedilemeyeceği öngörülen diğer ödemeler.</li>
          </ul>
          <p>Haczi caiz olmayan mal ve haklar hakkında borçlunun <strong>önceden</strong> yaptığı feragat geçerli değildir.</p>

          <h2>Maaş haczine itiraz</h2>
          <p>Kanuna aykırı oranda kesinti yapılması, haczedilemez bir gelire haciz konulması veya takibin kendisindeki usulsüzlükler nedeniyle, işlemin öğrenilmesinden itibaren <strong>yedi gün</strong> içinde icra mahkemesine şikâyet yoluna başvurulabilir (İİK m. 16). Takibin dayanağı olan borca itiraz edilmemişse, önce <a href="icra-takibine-itiraz-nasil-yapilir.html">icra takibine itiraz</a> sürelerinin geçip geçmediğine bakılmalıdır.</p>

          <h2>Borç ödenirse haciz ne zaman kalkar?</h2>
          <p>Borcun tamamı faiz ve masraflarıyla ödendiğinde alacaklı veya icra dairesi, işverene <strong>haczin kaldırılması</strong> yazısı gönderir. Borçlunun, ödeme belgelerini saklaması ve haczin kaldırıldığını işverenden teyit etmesi önerilir.</p>
""",
  },
  # ------------------------------------------------------------------ GAYRİMENKUL
  {
    "slug": "tapu-iptal-ve-tescil-davasi.html",
    "cat": "Gayrimenkul Hukuku", "tarih": "2026-11-17", "read": "6 dk okuma",
    "title": "Tapu İptal ve Tescil Davası | Gelegen Hukuk Bürosu",
    "desc": "Tapu iptal ve tescil davası sebepleri: muris muvazaası, vekâletin kötüye kullanılması, ehliyetsizlik. Görevli mahkeme, zamanaşımı ve tedbir. Gelegen Hukuk, Malatya.",
    "h1": "Tapu İptal ve Tescil Davası",
    "lead": "Tapu kaydının hukuka aykırı biçimde oluştuğu durumlarda gerçek hak sahibi, kaydın iptalini ve taşınmazın kendi adına tescilini isteyebilir. Bu yazıda tapu iptal ve tescil davasının başlıca sebeplerini ve sürecini özetliyoruz.",
    "body": """
          <h2>Tapu iptal ve tescil davası nedir?</h2>
          <p>Tapu sicilindeki bir kaydın <strong>yolsuz</strong>, yani geçerli bir hukuki sebebe dayanmadan oluştuğu durumlarda, ayni hakkı zedelenen kişi kaydın düzeltilmesini isteyebilir (TMK m. 1025). Dava, hem mevcut kaydın iptalini hem de taşınmazın davacı adına tescilini amaçlar.</p>

          <h2>Başlıca dava sebepleri</h2>
          <h3>1. Muris muvazaası (mirastan mal kaçırma)</h3>
          <p>Miras bırakanın, mirasçılarından mal kaçırmak amacıyla gerçekte <strong>bağışladığı</strong> bir taşınmazı tapuda <strong>satış</strong> gibi göstermesidir. Yargıtay'ın 1 Nisan 1974 tarihli İçtihadı Birleştirme Kararı uyarınca saklı payı bulunsun bulunmasın tüm mirasçılar bu davayı açabilir. Satış bedelinin taşınmazın gerçek değeriyle orantısız olması, alıcının ödeme gücünün bulunmaması ve tarafların yakınlığı gibi durumlar muvazaaya işaret edebilir.</p>
          <h3>2. Vekâletin kötüye kullanılması</h3>
          <p>Vekilin, vekâlet verenin aleyhine ve üçüncü kişiyle anlaşarak taşınmazı değerinin çok altında veya kendisine ya da yakınlarına devretmesi hâlinde tapu iptali istenebilir.</p>
          <h3>3. Ehliyetsizlik</h3>
          <p>Taşınmazı devreden kişinin işlem tarihinde <strong>ayırt etme gücünden yoksun</strong> olması (ör. ileri derecede demans) hâlinde işlem geçersizdir. Bu durum çoğunlukla Adli Tıp raporu ile ispat edilir.</p>
          <h3>4. İrade sakatlıkları</h3>
          <p>Hata, aldatma (hile) veya korkutma (ikrah) yoluyla yapılan devirlerde de tapu iptali gündeme gelebilir.</p>
          <h3>5. Diğer sebepler</h3>
          <ul>
            <li>Ölünceye kadar bakma sözleşmesinde bakım borcunun yerine getirilmemesi,</li>
            <li>Kazandırıcı zamanaşımı şartlarının oluşması (TMK m. 713),</li>
            <li>Sahte belge veya sahte kimlikle yapılan devirler.</li>
          </ul>

          <h2>Görevli ve yetkili mahkeme</h2>
          <p>Tapu iptal ve tescil davalarında görevli mahkeme kural olarak <strong>asliye hukuk mahkemesidir</strong>. Taşınmaz üzerindeki ayni haklara ilişkin olduğu için dava, <strong>kesin yetki</strong> kuralı gereği taşınmazın bulunduğu yer mahkemesinde açılır. Malatya'daki bir taşınmaz için dava Malatya'da görülür.</p>

          <h2>Zamanaşımı</h2>
          <ul>
            <li><strong>Muris muvazaası</strong> ve ehliyetsizliğe dayanan davalar zamanaşımına tabi değildir.</li>
            <li><strong>Hata ve aldatmaya</strong> dayanan iptal talepleri, yanılma veya aldatmanın öğrenildiği tarihten itibaren <strong>bir yıl</strong> içinde ileri sürülmelidir (TBK m. 39).</li>
          </ul>

          <h2>Dava sırasında tedbir</h2>
          <p>Dava süresince taşınmazın üçüncü kişilere devredilmesi, iyiniyetli alıcılar nedeniyle davayı sonuçsuz bırakabilir. Bu nedenle dava açılırken tapu kaydına <strong>ihtiyati tedbir şerhi</strong> konulması talep edilmelidir.</p>

          <h2>Masraflar</h2>
          <p>Tapu iptal ve tescil davalarında harç ve vekâlet ücreti, taşınmazın <strong>değeri</strong> esas alınarak hesaplanır. Taşınmazın değeri yargılama sırasında bilirkişi incelemesiyle belirlenir. Paylı taşınmazlarda dava sonrası <a href="ortakligin-giderilmesi-davasi.html">ortaklığın giderilmesi</a> de gündeme gelebilir.</p>
""",
  },
  # ------------------------------------------------------------------ MİRAS
  {
    "slug": "miras-paylasimi-ve-miras-paylari.html",
    "cat": "Miras Hukuku", "tarih": "2026-11-17", "read": "6 dk okuma",
    "title": "Miras Paylaşımı: Kim Ne Kadar Miras Alır? | Gelegen Hukuk Bürosu",
    "desc": "Yasal mirasçılar ve miras payları: çocuklar, eş, anne-baba, kardeşler. Eşin miras payı, örnek hesaplamalar ve veraset ve intikal vergisi. Gelegen Hukuk, Malatya.",
    "h1": "Miras Paylaşımı: Kim Ne Kadar Miras Alır?",
    "lead": "Vasiyetname bırakılmamışsa miras, Türk Medeni Kanunu'nda belirlenen yasal mirasçılar arasında kanuni paylara göre paylaştırılır. Bu yazıda mirasçılık sırasını ve payların nasıl hesaplandığını örneklerle açıklıyoruz.",
    "body": """
          <h2>Zümre sistemi</h2>
          <p>Türk hukukunda kan hısımları <strong>zümre</strong> esasına göre mirasçı olur. Önceki zümrede mirasçı varsa sonraki zümre mirasçı olamaz.</p>
          <ul>
            <li><strong>1. zümre — Altsoy (TMK m. 495):</strong> Çocuklar eşit paylarla mirasçı olur. Miras bırakandan önce ölmüş çocuğun yerini kendi çocukları (torunlar) alır. Evlatlıklar da öz çocuk gibi mirasçıdır.</li>
            <li><strong>2. zümre — Anne ve baba (TMK m. 496):</strong> Altsoy yoksa miras anne ve babaya eşit olarak kalır. Önceden ölmüş anne veya babanın yerini onun altsoyu, yani miras bırakanın <strong>kardeşleri</strong> alır.</li>
            <li><strong>3. zümre — Büyükanne ve büyükbabalar (TMK m. 497):</strong> İlk iki zümrede mirasçı yoksa miras büyükanne ve büyükbabalara, onların yerine de altsoylarına (amca, hala, dayı, teyze) geçer.</li>
          </ul>

          <h2>Sağ kalan eşin miras payı</h2>
          <p>Eş, zümrelerden hangisiyle birlikte mirasçı olduğuna göre farklı pay alır (TMK m. 499):</p>
          <ul>
            <li><strong>Çocuklarla birlikte:</strong> Mirasın <strong>dörtte biri</strong>,</li>
            <li><strong>Anne-baba zümresiyle birlikte:</strong> Mirasın <strong>yarısı</strong>,</li>
            <li><strong>Büyükanne-büyükbaba zümresiyle birlikte:</strong> Mirasın <strong>dörtte üçü</strong>,</li>
            <li>Bunlar da yoksa mirasın <strong>tamamı</strong>.</li>
          </ul>

          <h2>Örnek hesaplamalar</h2>
          <ul>
            <li><strong>Eş + 2 çocuk:</strong> Eş 1/4; kalan 3/4 iki çocuk arasında eşit paylaşılır, her çocuk 3/8 alır.</li>
            <li><strong>Eş + anne + baba (çocuk yok):</strong> Eş 1/2; anne ve baba kalan yarıyı paylaşır, her biri 1/4 alır.</li>
            <li><strong>Eş + anne (baba önceden ölmüş) + 2 kardeş:</strong> Eş 1/2; anne 1/4; babanın payı olan 1/4 kardeşlere geçer, her kardeş 1/8 alır.</li>
            <li><strong>Yalnızca 3 çocuk:</strong> Her çocuk 1/3 alır.</li>
          </ul>

          <h2>Vasiyetname varsa ne olur?</h2>
          <p>Miras bırakan, <a href="vasiyetname-nasil-yapilir.html">vasiyetname</a> ile paylaşımı değiştirebilir; ancak altsoy, anne-baba ve eşin <strong>saklı paylarına</strong> dokunamaz. Saklı payı zedelenen mirasçı tenkis davası açabilir. Kardeşlerin saklı payı yoktur.</p>

          <h2>Paylaşım nasıl yapılır?</h2>
          <ol>
            <li><strong>Mirasçılık belgesi</strong> notere veya sulh hukuk mahkemesine başvurularak alınır.</li>
            <li>Mirasçılar terekenin borçlu olup olmadığını araştırır; borca batık terekelerde <a href="mirasin-reddi-ve-mirascilik-belgesi.html">mirasın reddi</a> için üç aylık süre gözetilir.</li>
            <li>Mirasçılar paylaşım üzerinde anlaşırsa yazılı bir <strong>paylaşma sözleşmesi</strong> yapılabilir ve tapuda intikal işlemleri buna göre tamamlanır.</li>
            <li>Anlaşma sağlanamazsa miras ortaklığı, sulh hukuk mahkemesinde açılacak <a href="ortakligin-giderilmesi-davasi.html">ortaklığın giderilmesi</a> davası ile sona erdirilir.</li>
          </ol>

          <h2>Veraset ve intikal vergisi</h2>
          <p>Mirasçılar, ölüm Türkiye'de gerçekleşmişse ölüm tarihini izleyen <strong>dört ay</strong> içinde vergi dairesine veraset ve intikal vergisi beyannamesi vermelidir. Belirli tutara kadar olan intikaller için istisnalar uygulanır; istisna tutarları her yıl yeniden belirlenir.</p>
""",
  },
  {
    "slug": "vasiyetname-nasil-yapilir.html",
    "cat": "Miras Hukuku", "tarih": "2026-11-17", "read": "5 dk okuma",
    "title": "Vasiyetname Nasıl Yapılır? Türleri ve Geçerlilik Şartları | Gelegen Hukuk Bürosu",
    "desc": "Resmî, el yazılı ve sözlü vasiyetname nasıl yapılır, geçerlilik şartları, saklı pay sınırı, vasiyetnamenin açılması ve iptali. Gelegen Hukuk, Malatya.",
    "h1": "Vasiyetname Nasıl Yapılır? Türleri ve Geçerlilik Şartları",
    "lead": "Vasiyetname, kişinin ölümünden sonra malvarlığının nasıl paylaşılacağını belirlemesini sağlayan tek taraflı bir hukuki işlemdir. Geçerli olabilmesi için kanundaki şekil şartlarına sıkı sıkıya uyulmalıdır. Bu yazıda vasiyetname türlerini özetliyoruz.",
    "body": """
          <h2>Kimler vasiyetname yapabilir?</h2>
          <p>Ayırt etme gücüne sahip ve <strong>15 yaşını doldurmuş</strong> herkes vasiyetname yapabilir (TMK m. 502). Vasiyetname yapanın, işlem anında ne yaptığını bilecek durumda olması gerekir.</p>

          <h2>Vasiyetname türleri</h2>
          <p>Türk Medeni Kanunu m. 531 uyarınca vasiyetname üç şekilde yapılabilir:</p>
          <h3>1. Resmî vasiyetname</h3>
          <p>Resmî memur (noter, sulh hâkimi veya kanunla yetkilendirilmiş başka bir görevli) önünde ve <strong>iki tanık</strong> katılımıyla yapılır (TMK m. 532 vd.). Vasiyetçi arzularını memura bildirir, memur vasiyetnameyi yazar; vasiyetçi okuyup imzalar ve tanıklar, vasiyetçinin beyanlarını kendi önlerinde yaptığını ve tasarrufa ehil göründüğünü onaylar. İspat ve saklama bakımından en güvenli yoldur.</p>
          <h3>2. El yazılı vasiyetname</h3>
          <p>Vasiyetnamenin <strong>baştan sona vasiyetçinin el yazısıyla</strong> yazılması, yapıldığı <strong>yıl, ay ve günün</strong> belirtilmesi ve <strong>imzalanması</strong> gerekir (TMK m. 538). Bilgisayarla yazılıp yalnızca imzalanan metin el yazılı vasiyetname sayılmaz. Vasiyetçi, el yazılı vasiyetnameyi açık veya kapalı olarak saklanmak üzere notere veya sulh hâkimine bırakabilir.</p>
          <h3>3. Sözlü vasiyetname</h3>
          <p>Ölüm tehlikesi, ulaşımın kesilmesi, salgın hastalık veya savaş gibi <strong>olağanüstü durumlarda</strong>, diğer şekillere başvurulamıyorsa iki tanığa sözlü olarak yapılır (TMK m. 539). Olağanüstü durum sona erdikten sonra vasiyetçi diğer şekillerde vasiyetname yapma imkânına kavuşur ve <strong>bir ay</strong> geçerse sözlü vasiyetname hükümsüz kalır.</p>

          <h2>Vasiyetnameyle neler yapılabilir?</h2>
          <ul>
            <li>Mirasçı atama veya belirli bir malı belirli bir kişiye bırakma (belirli mal bırakma),</li>
            <li>Bir vakıf kurulması veya bir kuruma bağış yapılması,</li>
            <li>Vasiyeti yerine getirme görevlisi atanması,</li>
            <li>Kanunda öngörülen sebeplerle mirasçılıktan çıkarma.</li>
          </ul>

          <h2>Saklı pay sınırı</h2>
          <p>Vasiyetname ile mirasçıların <strong>saklı paylarına</strong> dokunulamaz. Altsoy, anne-baba ve eşin saklı payını ihlal eden vasiyetname geçersiz olmaz, ancak saklı payı zedelenen mirasçı <strong>tenkis davası</strong> açarak payını isteyebilir. Ayrıntılar için <a href="miras-paylasimi-ve-miras-paylari.html">miras paylaşımı</a> yazımıza bakabilirsiniz.</p>

          <h2>Vasiyetnamenin açılması</h2>
          <p>Vasiyetçinin ölümünden sonra, eline vasiyetname geçen kişi bunu <strong>derhal sulh hâkimine</strong> teslim etmek zorundadır (TMK m. 595). Sulh hâkimi vasiyetnameyi bir ay içinde açar ve mirasçılara okur; ilgililere birer örneğini tebliğ eder.</p>

          <h2>Vasiyetnamenin iptali</h2>
          <p>Vasiyetçinin tasarruf ehliyetinin bulunmaması, iradesinin yanılma, aldatma veya korkutma ile sakatlanması, içeriğin hukuka veya ahlaka aykırı olması ya da şekil şartlarına uyulmaması hâlinde vasiyetnamenin iptali istenebilir (TMK m. 557). Dava, iptal sebebinin ve davacının hak sahibi olduğunun öğrenilmesinden itibaren <strong>bir yıl</strong>, her hâlde vasiyetnamenin açılmasından itibaren <strong>on yıl</strong> içinde açılmalıdır.</p>
""",
  },
  # ------------------------------------------------------------------ İDARE
  {
    "slug": "iptal-davasi-nasil-acilir.html",
    "cat": "İdare Hukuku", "tarih": "2026-11-17", "read": "5 dk okuma",
    "title": "İdari İşlemlere Karşı İptal Davası Nasıl Açılır? | Gelegen Hukuk Bürosu",
    "desc": "İptal davası nedir, dava açma süresi (60 gün, vergi 30 gün), üst makama başvuru, yürütmenin durdurulması, istinaf ve temyiz. Gelegen Hukuk, Malatya.",
    "h1": "İdari İşlemlere Karşı İptal Davası Nasıl Açılır?",
    "lead": "Kamu kurumlarının hukuka aykırı işlemlerine karşı en etkili yol, idare mahkemesinde açılacak iptal davasıdır. Atama, disiplin cezası, ruhsat iptali veya imar işlemleri gibi pek çok işlem bu yolla denetlenebilir. Bu yazıda süreci özetliyoruz.",
    "body": """
          <h2>İptal davası nedir?</h2>
          <p>İdari Yargılama Usulü Kanunu (İYUK) m. 2 uyarınca iptal davası, idari işlemlerin <strong>yetki, şekil, sebep, konu ve maksat</strong> yönlerinden biriyle hukuka aykırı olduğu ileri sürülerek, <strong>menfaati ihlal edilenler</strong> tarafından açılan davadır. Mahkeme işlemi hukuka aykırı bulursa iptal eder ve işlem, yapıldığı andan itibaren hükümsüz hâle gelir.</p>

          <h2>Hangi işlemlere karşı açılabilir?</h2>
          <ul>
            <li>Kamu görevlilerinin atama, görevden alma, disiplin ve sicil işlemleri,</li>
            <li>İmar planları, yapı ruhsatı ve yıkım kararları,</li>
            <li>İşyeri açma ve çalışma ruhsatlarının iptali,</li>
            <li>Sınav, öğrenci ve akademik işlemler,</li>
            <li>İhale işlemleri ve diğer kesin ve yürütülmesi gereken idari işlemler.</li>
          </ul>

          <h2>Dava açma süresi</h2>
          <ul>
            <li><strong>İdare mahkemelerinde:</strong> Özel kanunlarda ayrı süre öngörülmedikçe <strong>60 gün</strong>,</li>
            <li><strong>Vergi mahkemelerinde:</strong> <strong>30 gün</strong> (İYUK m. 7).</li>
          </ul>
          <p>Süre, işlemin ilgiliye <strong>yazılı bildirim</strong> tarihinden itibaren başlar. İlanı gereken düzenleyici işlemlerde süre ilan tarihinden itibaren işler. Süresinde açılmayan dava esasa girilmeden reddedilir.</p>

          <h2>Üst makama başvuru</h2>
          <p>İlgililer, dava açmadan önce işlemin kaldırılması, geri alınması veya değiştirilmesini dava açma süresi içinde <strong>üst makamdan</strong> (yoksa işlemi yapan makamdan) isteyebilir. Bu başvuru, işlemekte olan dava açma süresini durdurur. Başvuruya <strong>30 gün</strong> içinde cevap verilmezse istek reddedilmiş sayılır; ret üzerine süre kaldığı yerden işlemeye devam eder (İYUK m. 11).</p>

          <h2>Yürütmenin durdurulması</h2>
          <p>Dava açmak işlemin uygulanmasını kendiliğinden durdurmaz. İşlemin uygulanması hâlinde <strong>telafisi güç veya imkânsız zararların</strong> doğması ve işlemin <strong>açıkça hukuka aykırı</strong> olması şartlarının birlikte gerçekleşmesi hâlinde mahkeme yürütmenin durdurulmasına karar verebilir (İYUK m. 27). Bu talep dava dilekçesinde gerekçesiyle birlikte ileri sürülmelidir.</p>

          <h2>Dava dilekçesi ve yargılama</h2>
          <p>Dava dilekçesinde tarafların bilgileri, dava konusu işlemin tarihi ve sayısı, tebliğ tarihi, olaylar ve hukuki sebepler yer almalı; işlemin bir örneği eklenmelidir. İdari yargıda yargılama kural olarak <strong>yazılı</strong> yürütülür ve dosya üzerinden incelenir; mahkeme gerekli gördüğünde keşif, bilirkişi incelemesi veya duruşma yapabilir.</p>

          <h2>Kanun yolları</h2>
          <p>İdare ve vergi mahkemesi kararlarına karşı tebliğden itibaren <strong>30 gün</strong> içinde bölge idare mahkemesine istinaf, kanunda sayılan kararlar için ise Danıştay'a temyiz yoluna başvurulabilir. İdari para cezalarının itiraz usulü farklıdır; ayrıntılar için <a href="idari-para-cezasina-itiraz.html">idari para cezasına itiraz</a> yazımıza bakabilirsiniz.</p>
""",
  },
  # ------------------------------------------------------------------ TAZMİNAT
  {
    "slug": "trafik-kazasi-tazminati.html",
    "cat": "Tazminat Hukuku", "tarih": "2026-11-17", "read": "6 dk okuma",
    "title": "Trafik Kazası Tazminatı: Hangi Haklar Talep Edilir? | Gelegen Hukuk Bürosu",
    "desc": "Trafik kazasında araç hasarı, değer kaybı, iş göremezlik, destekten yoksun kalma ve manevi tazminat; sigortaya başvuru, tahkim ve zamanaşımı. Gelegen Hukuk, Malatya.",
    "h1": "Trafik Kazası Tazminatı: Hangi Haklar Talep Edilir?",
    "lead": "Trafik kazası sonrasında zarar görenler, araç hasarından yaralanmaya ve yakın kaybına kadar farklı kalemlerde tazminat isteyebilir. Bu yazıda talep edilebilecek tazminatları, sigortaya başvuru zorunluluğunu ve süreleri özetliyoruz.",
    "body": """
          <h2>Kimden tazminat istenir?</h2>
          <p>Karayolları Trafik Kanunu (KTK) m. 85 uyarınca motorlu aracın işletilmesi bir kişinin ölümüne, yaralanmasına veya bir şeyin zarara uğramasına sebep olursa, aracın <strong>işleteni</strong> ve bağlı olduğu teşebbüs sahibi müteselsilen sorumlu olur. Uygulamada tazminat, aracın <strong>zorunlu mali sorumluluk (trafik) sigortası</strong> şirketinden, poliçe limitleri dahilinde talep edilir. Limiti aşan zararlar için sürücü ve işletene başvurulabilir.</p>

          <h2>Talep edilebilecek tazminat kalemleri</h2>
          <h3>Maddi hasar</h3>
          <ul>
            <li><strong>Araç hasarı:</strong> Onarım masrafları veya tam hasar durumunda aracın değeri,</li>
            <li><strong>Değer kaybı:</strong> Kaza sonrası onarılan aracın piyasa değerindeki düşüş,</li>
            <li><strong>Araç mahrumiyeti (kazanç kaybı):</strong> Aracın serviste kaldığı süre için ikame araç veya kazanç kaybı.</li>
          </ul>
          <h3>Bedensel zarar</h3>
          <ul>
            <li><strong>Tedavi giderleri,</strong></li>
            <li><strong>Geçici iş göremezlik:</strong> Tedavi süresince çalışamamaktan doğan kayıp,</li>
            <li><strong>Sürekli iş göremezlik (maluliyet):</strong> Kalıcı sakatlık oranına göre hesaplanan tazminat,</li>
            <li><strong>Bakıcı giderleri.</strong></li>
          </ul>
          <h3>Ölüm hâlinde</h3>
          <ul>
            <li><strong>Destekten yoksun kalma tazminatı:</strong> Ölenin desteğinden yoksun kalan eş, çocuklar ve diğer yakınlar için,</li>
            <li><strong>Cenaze giderleri.</strong></li>
          </ul>
          <h3>Manevi tazminat</h3>
          <p>Yaralanan kişi ve ölüm hâlinde yakınları manevi tazminat isteyebilir. Ancak manevi tazminat <strong>zorunlu trafik sigortasının kapsamında değildir</strong>; bu talep sürücü, işleten veya (kaskoda ihtiyari teminat varsa) ilgili sigorta şirketine yöneltilir.</p>

          <h2>Kusur oranının önemi</h2>
          <p>Tazminat miktarı, kaza tespit tutanağı ve bilirkişi raporlarıyla belirlenen <strong>kusur oranına</strong> göre hesaplanır. Zarar görenin de kusuru varsa tazminattan bu oranda indirim yapılır. Tutanaktaki kusur tespitine katılmıyorsanız, yargılama sırasında bilirkişi incelemesiyle bu tespit tartışılabilir.</p>

          <h2>Önce sigortaya başvuru zorunlu</h2>
          <p>Zarar gören, dava açmadan veya tahkime başvurmadan önce <strong>sigorta şirketine yazılı olarak başvurmak</strong> zorundadır (KTK m. 97). Sigorta şirketi <strong>15 gün</strong> içinde başvuruyu sonuçlandırmazsa veya ödeme teklifini kabul etmezseniz:</p>
          <ul>
            <li>Asliye ticaret veya asliye hukuk mahkemesinde dava açabilir,</li>
            <li>Ya da <strong>Sigorta Tahkim Komisyonuna</strong> başvurabilirsiniz.</li>
          </ul>
          <p>Kazaya karışan araç sigortasızsa veya kaçmışsa, belirli zararlar için <strong>Güvence Hesabına</strong> başvurulabilir.</p>

          <h2>Zamanaşımı</h2>
          <p>Trafik kazasından doğan tazminat talepleri, zarar görenin zararı ve tazminat yükümlüsünü öğrendiği tarihten itibaren <strong>iki yıl</strong>, her hâlde kaza tarihinden itibaren <strong>on yıl</strong> içinde zamanaşımına uğrar. Kaza aynı zamanda ceza kanunlarına göre daha uzun zamanaşımına tabi bir suç oluşturuyorsa (ör. taksirle yaralama), bu uzun süre uygulanır (KTK m. 109).</p>
""",
  },
]
