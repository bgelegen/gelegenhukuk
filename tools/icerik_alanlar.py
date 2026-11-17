# -*- coding: utf-8 -*-
"""
Çalışma alanı sayfalarının içeriği. Her alan bir sayfa üretir: <slug>.
Dil: Avukatlık Kanunu m. 55 ve TBB Reklam Yasağı Yönetmeliği'ne uygun, yalnızca
bilgilendirici. "En iyi", başarı oranı, sonuç vaadi YOK.
'kategori' alanı, makalelerdeki 'cat' ile eşleşir (ilgili yazılar listesi için).
"""

ALANLAR = [
  {
    "slug": "malatya-bosanma-avukati.html",
    "kisa": "Aile ve Boşanma Hukuku",
    "kategori": "Aile Hukuku",
    "title": "Malatya Boşanma Avukatı | Aile Hukuku | Gelegen Hukuk Bürosu",
    "desc": "Malatya'da anlaşmalı ve çekişmeli boşanma, nafaka, velayet ve mal paylaşımı davaları hakkında bilgi. Gelegen Hukuk Bürosu, Battalgazi / Malatya.",
    "h1": "Malatya Boşanma Avukatı ve Aile Hukuku",
    "lead": "Boşanma ve aile uyuşmazlıkları, hem hukuki hem kişisel yönüyle dikkatli yürütülmesi gereken süreçlerdir. Malatya Aile Mahkemelerinde görülen davalarda süreç, belgeler ve haklar hakkında bilmeniz gerekenleri bu sayfada özetledik.",
    "kart": "Anlaşmalı ve çekişmeli boşanma, velayet, nafaka, mal rejiminin tasfiyesi ve koruma kararları.",
    "body": """
          <h2>Aile hukukunda hangi konularda destek veriyoruz?</h2>
          <ul>
            <li><strong>Anlaşmalı boşanma:</strong> Boşanma protokolünün hazırlanması ve tek duruşmada sonuçlanması hedeflenen süreçlerin takibi.</li>
            <li><strong>Çekişmeli boşanma:</strong> Türk Medeni Kanunu'ndaki özel ve genel boşanma sebeplerine dayanan davalar; delil ve tanık listelerinin hazırlanması.</li>
            <li><strong>Velayet ve kişisel ilişki:</strong> Velayetin belirlenmesi, değiştirilmesi ve çocukla kişisel ilişki düzenlemesi.</li>
            <li><strong>Nafaka:</strong> Tedbir, iştirak ve yoksulluk nafakası; nafakanın artırılması, azaltılması veya kaldırılması davaları.</li>
            <li><strong>Mal rejiminin tasfiyesi:</strong> Edinilmiş mallara katılma alacağı ve katkı payı alacağı davaları.</li>
            <li><strong>Maddi ve manevi tazminat:</strong> Boşanmaya bağlı tazminat talepleri.</li>
            <li><strong>6284 sayılı Kanun kapsamında koruma kararları</strong> ve yurt dışında verilen boşanma kararlarının <strong>tanınması ve tenfizi</strong>.</li>
          </ul>

          <h2>Malatya'da boşanma davası nerede açılır?</h2>
          <p>Boşanma davalarında görevli mahkeme <strong>aile mahkemesidir</strong>. Aile mahkemesi bulunmayan yerlerde davaya asliye hukuk mahkemesi aile mahkemesi sıfatıyla bakar. Türk Medeni Kanunu m. 168 uyarınca dava; eşlerden birinin yerleşim yeri veya eşlerin davadan önce <strong>son altı aydan beri birlikte oturdukları yer</strong> mahkemesinde açılabilir. Malatya'da oturan ya da son altı ayını Malatya'da geçirmiş eşler davayı Malatya'da açabilir.</p>

          <h2>Boşanma süreci nasıl ilerler?</h2>
          <ol>
            <li><strong>Ön görüşme ve belge incelemesi:</strong> Evlilik süresi, çocukların durumu, mal varlığı ve deliller değerlendirilir.</li>
            <li><strong>Yol seçimi:</strong> Şartlar uygunsa anlaşmalı boşanma, değilse çekişmeli boşanma yolu belirlenir.</li>
            <li><strong>Dilekçe ve tedbir talepleri:</strong> Dava açılırken tedbir nafakası, çocukla geçici kişisel ilişki gibi talepler de ileri sürülebilir.</li>
            <li><strong>Ön inceleme ve tahkikat:</strong> Çekişmeli davalarda tanıklar dinlenir; gerekirse sosyal inceleme raporu alınır.</li>
            <li><strong>Karar ve kesinleşme:</strong> Karar, kanun yollarına başvurulmazsa ya da başvurular sonuçlanınca kesinleşir ve nüfusa işlenir.</li>
          </ol>

          <h2>Boşanma davasında süreler önemlidir</h2>
          <p>Bazı boşanma sebepleri hak düşürücü sürelere bağlıdır. Örneğin zina ve hayata kast, pek kötü veya onur kırıcı davranış sebeplerine dayanan davalarda, sebebin öğrenilmesinden itibaren <strong>altı ay</strong> ve her hâlde olayın üzerinden <strong>beş yıl</strong> geçmekle dava hakkı düşer. Boşanmadan doğan tazminat ve nafaka gibi dava hakları da boşanma kararının kesinleşmesinden itibaren <strong>bir yıl</strong> içinde zamanaşımına uğrar (TMK m. 178).</p>
""",
    "sss": [
      ("Malatya'da anlaşmalı boşanma ne kadar sürer?",
       "Anlaşmalı boşanma genellikle tek duruşmada sonuçlanır. Toplam süre; duruşma gününün ne zamana verildiğine, kararın yazılmasına ve kesinleşme sürecine göre değişir."),
      ("Boşanma davası için iki eşin de duruşmaya gelmesi gerekir mi?",
       "Anlaşmalı boşanmada hâkimin tarafları bizzat dinlemesi gerektiğinden her iki eşin de duruşmada hazır bulunması zorunludur. Çekişmeli davalarda taraflar avukatları aracılığıyla temsil edilebilir."),
      ("Velayet kimde kalır?",
       "Velayet kararında belirleyici ölçüt çocuğun üstün yararıdır. Mahkeme; çocuğun yaşı, bakım ihtiyacı, ebeveynlerin koşulları ve idrak çağındaki çocuğun görüşü gibi unsurları birlikte değerlendirir."),
      ("Boşanma davasında nafaka ne zaman istenebilir?",
       "Tedbir nafakası dava süresince, iştirak ve yoksulluk nafakası ise boşanma kararıyla birlikte talep edilebilir. Yoksulluk nafakası boşanma kararıyla istenmemişse, karar kesinleştikten sonra bir yıl içinde ayrı davayla istenebilir."),
    ],
  },
  {
    "slug": "malatya-ceza-avukati.html",
    "kisa": "Ceza Hukuku",
    "kategori": "Ceza Hukuku",
    "title": "Malatya Ceza Avukatı | Ceza Hukuku | Gelegen Hukuk Bürosu",
    "desc": "Malatya'da soruşturma ve kovuşturma aşamalarında müdafilik, mağdur vekilliği, istinaf ve temyiz süreçleri hakkında bilgi. Gelegen Hukuk Bürosu, Malatya.",
    "h1": "Malatya Ceza Avukatı ve Ceza Hukuku",
    "lead": "Ceza yargılamasında ilk ifadeden kararın kesinleşmesine kadar her aşama, kişinin özgürlüğünü ve geleceğini doğrudan etkiler. Malatya'daki soruşturma ve kovuşturma süreçlerine ilişkin temel bilgileri bu sayfada bulabilirsiniz.",
    "kart": "Soruşturma ve kovuşturmada şüpheli/sanık müdafiliği, mağdur ve katılan vekilliği, kanun yolları.",
    "body": """
          <h2>Ceza hukukunda hangi konularda destek veriyoruz?</h2>
          <ul>
            <li><strong>Soruşturma aşaması:</strong> Kolluk ve savcılık ifadelerinde, gözaltı ve tutuklama süreçlerinde şüpheli müdafiliği.</li>
            <li><strong>Kovuşturma aşaması:</strong> Asliye ceza ve ağır ceza mahkemelerinde sanık müdafiliği.</li>
            <li><strong>Mağdur ve katılan vekilliği:</strong> Suçtan zarar görenlerin şikâyet, davaya katılma ve tazminat süreçleri.</li>
            <li><strong>Tutukluluğa itiraz</strong> ve adli kontrol kararlarına itiraz başvuruları.</li>
            <li><strong>Kanun yolları:</strong> İstinaf ve temyiz başvuruları, hükmün açıklanmasının geri bırakılması (HAGB) kararlarına itiraz.</li>
            <li><strong>Uzlaştırma</strong> süreçlerinde temsil ve yeniden yargılama başvuruları.</li>
          </ul>

          <h2>Gözaltında ve ifadede avukat hakkı</h2>
          <p>Ceza Muhakemesi Kanunu (CMK) m. 149 uyarınca şüpheli veya sanık, soruşturma ve kovuşturmanın her aşamasında bir veya birden fazla <strong>müdafi</strong> yardımından yararlanabilir. Gözaltındaki kişinin avukatıyla görüşme hakkı kısıtlanamaz. Şüpheli; 18 yaşından küçükse, kendisini savunamayacak derecede malulse ya da alt sınırı beş yıldan fazla hapis cezasını gerektiren bir suçtan dolayı yargılanıyorsa ve müdafi seçmemişse, istemi aranmaksızın baro tarafından müdafi görevlendirilir (CMK m. 150).</p>
          <p>İfade vermeden önce suçlamanın içeriğini öğrenmek, susma hakkının bulunduğunu bilmek ve avukatla görüşmek, savunmanın sağlıklı kurulabilmesi için önemlidir.</p>

          <h2>Ceza davası hangi mahkemede görülür?</h2>
          <p>Kanunda üst sınırı on yıldan fazla hapis cezasını gerektiren suçlar ile özel olarak belirtilen suçlarda <strong>ağır ceza mahkemesi</strong>, diğer suçlarda <strong>asliye ceza mahkemesi</strong> görevlidir. Kural olarak yetkili mahkeme, suçun işlendiği yer mahkemesidir; Malatya'da işlendiği iddia edilen suçlara ilişkin davalar Malatya'daki ceza mahkemelerinde görülür.</p>

          <h2>Ceza yargılaması nasıl ilerler?</h2>
          <ol>
            <li><strong>Soruşturma:</strong> Şikâyet veya ihbarla başlar; savcılık delilleri toplar ve kovuşturmaya yer olmadığına ya da iddianame düzenlenmesine karar verir.</li>
            <li><strong>İddianamenin kabulü:</strong> Mahkeme iddianameyi kabul ederse kovuşturma aşaması başlar.</li>
            <li><strong>Duruşmalar:</strong> Sanık savunması alınır, tanıklar dinlenir, deliller tartışılır.</li>
            <li><strong>Hüküm:</strong> Beraat, mahkûmiyet, HAGB veya düşme gibi kararlar verilebilir.</li>
            <li><strong>Kanun yolları:</strong> Karar türüne göre istinaf, temyiz veya itiraz yoluna başvurulabilir.</li>
          </ol>
""",
    "sss": [
      ("Gözaltına alınan yakınım için avukat ne zaman devreye girebilir?",
       "Avukat, gözaltının başından itibaren şüpheliyle görüşebilir ve ifade sırasında hazır bulunabilir. Bu hak, kanunda sayılan istisnalar dışında kısıtlanamaz."),
      ("Ağır ceza ile asliye ceza mahkemesi arasındaki fark nedir?",
       "Ağır ceza mahkemeleri kural olarak üst sınırı on yıldan fazla hapis cezasını gerektiren suçlara, asliye ceza mahkemeleri ise diğer suçlara bakar. Görev, iddia edilen suçun kanundaki cezasına göre belirlenir."),
      ("Ceza davasında istinaf süresi ne kadardır?",
       "İstinaf başvuru süresi, hükmün açıklanmasından, yokluğunda verilen hükümlerde ise tebliğden itibaren iki haftadır (CMK m. 273). Sürenin kaçırılması hâlinde karar kesinleşebilir."),
      ("Şikâyetten vazgeçilirse dava düşer mi?",
       "Yalnızca şikâyete bağlı suçlarda şikâyetten vazgeçme davayı düşürür. Kamu davası niteliğindeki suçlarda şikâyetten vazgeçmek yargılamayı sona erdirmez."),
    ],
  },
  {
    "slug": "malatya-is-hukuku-avukati.html",
    "kisa": "İş Hukuku",
    "kategori": "İş Hukuku",
    "title": "Malatya İş Hukuku Avukatı | İşçi ve İşveren | Gelegen Hukuk Bürosu",
    "desc": "Malatya'da işe iade, kıdem ve ihbar tazminatı, fazla mesai, iş kazası ve zorunlu arabuluculuk süreçleri hakkında bilgi. Gelegen Hukuk Bürosu, Malatya.",
    "h1": "Malatya İş Hukuku Avukatı",
    "lead": "İş ilişkisinin sona ermesi, ödenmeyen ücretler veya iş kazası gibi durumlarda hak kaybı yaşamamak için sürelerin ve zorunlu arabuluculuk aşamasının doğru yönetilmesi gerekir. İşçi ve işveren tarafı için temel bilgileri bu sayfada derledik.",
    "kart": "İşe iade, kıdem ve ihbar tazminatı, işçilik alacakları, iş kazası ve hizmet tespiti davaları.",
    "body": """
          <h2>İş hukukunda hangi konularda destek veriyoruz?</h2>
          <ul>
            <li><strong>İşe iade davaları</strong> ve işe başlatmama tazminatı.</li>
            <li><strong>Kıdem ve ihbar tazminatı</strong> talepleri.</li>
            <li><strong>İşçilik alacakları:</strong> Fazla mesai, hafta tatili, genel tatil ve yıllık izin ücreti.</li>
            <li><strong>İş kazası ve meslek hastalığı</strong> nedeniyle maddi ve manevi tazminat davaları.</li>
            <li><strong>Hizmet tespit davaları:</strong> Sigortasız geçen çalışmaların tespiti.</li>
            <li><strong>İşveren danışmanlığı:</strong> İş sözleşmeleri, fesih süreçleri, iç yönetmelikler ve disiplin uygulamaları.</li>
          </ul>

          <h2>Dava açmadan önce zorunlu arabuluculuk</h2>
          <p>Kanuna, bireysel veya toplu iş sözleşmesine dayanan işçi veya işveren alacağı ve tazminatı ile işe iade taleplerinde, dava açılmadan önce <strong>arabulucuya başvurulması zorunludur</strong> (7036 sayılı İş Mahkemeleri Kanunu m. 3). Arabuluculuğa başvurmadan açılan dava usulden reddedilir. İş kazası veya meslek hastalığından kaynaklanan tazminat davaları ile hizmet tespiti davaları ise zorunlu arabuluculuk kapsamında değildir.</p>

          <h2>İş davalarında dikkat edilmesi gereken süreler</h2>
          <ul>
            <li><strong>İşe iade:</strong> Fesih bildiriminin tebliğinden itibaren <strong>bir ay</strong> içinde arabulucuya başvurulmalıdır.</li>
            <li><strong>Kıdem ve ihbar tazminatı, ücret ve diğer işçilik alacakları:</strong> Kural olarak <strong>beş yıllık</strong> zamanaşımı süresine tabidir.</li>
            <li><strong>Hizmet tespiti:</strong> Hizmetin geçtiği yılın sonundan itibaren <strong>beş yıl</strong> içinde dava açılmalıdır.</li>
          </ul>

          <h2>Malatya'da iş davası nerede görülür?</h2>
          <p>İş uyuşmazlıklarında görevli mahkeme <strong>iş mahkemesidir</strong>; iş mahkemesi bulunmayan yerlerde asliye hukuk mahkemesi bu sıfatla bakar. Dava, davalının yerleşim yeri veya işin ya da işlemin yapıldığı yer mahkemesinde açılabilir. Malatya'da çalışılan işyerlerine ilişkin uyuşmazlıklar Malatya iş mahkemelerinde görülebilir.</p>
""",
    "sss": [
      ("İşten çıkarıldım, kıdem tazminatı alabilir miyim?",
       "Aynı işverene bağlı olarak en az bir yıl çalışmış olmanız ve iş sözleşmesinin kanunda sayılan hâllerden biriyle sona ermesi gerekir. İşverenin ahlak ve iyi niyet kurallarına uymayan davranışlar nedeniyle haklı feshi gibi durumlarda kıdem tazminatı ödenmez."),
      ("İstifa eden işçi kıdem tazminatı alabilir mi?",
       "Kural olarak hayır; ancak işçinin haklı nedenle feshi (ör. ücretin ödenmemesi), askerlik, emeklilik veya kadın işçinin evlendikten sonra bir yıl içinde ayrılması gibi hâllerde kıdem tazminatına hak kazanılabilir."),
      ("Arabuluculukta anlaşma sağlanırsa dava açabilir miyim?",
       "Arabuluculuk sonunda anlaşılan konular hakkında taraflar sonradan dava açamaz. Bu nedenle anlaşma tutanağının kapsamı imzadan önce dikkatle incelenmelidir."),
      ("İş kazasında kimden tazminat istenir?",
       "İş kazasında işverenin kusuru oranında maddi ve manevi tazminat talep edilebilir. Ayrıca Sosyal Güvenlik Kurumu tarafından sağlanan geçici iş göremezlik ödeneği ve gelir bağlanması gibi haklar ayrıca değerlendirilir."),
    ],
  },
  {
    "slug": "malatya-icra-avukati.html",
    "kisa": "İcra ve İflas Hukuku",
    "kategori": "İcra ve İflas Hukuku",
    "title": "Malatya İcra Avukatı | İcra ve İflas Hukuku | Gelegen Hukuk Bürosu",
    "desc": "Malatya'da icra takibi, ödeme emrine itiraz, kambiyo senetleri, haciz, itirazın iptali ve menfi tespit davaları hakkında bilgi. Gelegen Hukuk Bürosu.",
    "h1": "Malatya İcra Avukatı ve İcra Hukuku",
    "lead": "Alacağın tahsili veya hakkınızda başlatılan bir takibe karşı savunma, kısa ve hak düşürücü sürelerle işleyen bir süreçtir. Malatya icra daireleri ve icra mahkemelerindeki işlemlere ilişkin temel bilgileri bu sayfada bulabilirsiniz.",
    "kart": "İlamlı ve ilamsız takipler, kambiyo takipleri, itirazın iptali, menfi tespit ve haciz işlemleri.",
    "body": """
          <h2>İcra hukukunda hangi konularda destek veriyoruz?</h2>
          <ul>
            <li><strong>Alacaklı tarafı:</strong> İlamsız takip, ilamlı takip, kambiyo senetlerine (çek, bono) dayalı takip, ihtiyati haciz.</li>
            <li><strong>Borçlu tarafı:</strong> Ödeme emrine itiraz, imzaya itiraz, şikâyet ve takibin iptali başvuruları.</li>
            <li><strong>Davalar:</strong> İtirazın iptali, itirazın kaldırılması, menfi tespit ve istirdat davaları.</li>
            <li><strong>Haciz ve satış:</strong> Haciz işlemleri, istihkak davaları, ihale ve satış süreçleri.</li>
            <li><strong>Kira alacağı ve tahliye</strong> için icra yoluyla takip.</li>
          </ul>

          <h2>Takip türlerine göre itiraz süreleri</h2>
          <ul>
            <li><strong>İlamsız takip:</strong> Ödeme emrinin tebliğinden itibaren <strong>7 gün</strong> içinde icra dairesine itiraz edilir.</li>
            <li><strong>Kambiyo senetlerine dayalı takip:</strong> Borca veya imzaya itiraz için <strong>5 gün</strong> içinde icra mahkemesine başvurulur; ödeme süresi 10 gündür.</li>
            <li><strong>Şikâyet:</strong> İcra memurunun işlemlerine karşı kural olarak öğrenmeden itibaren <strong>7 gün</strong> içinde icra mahkemesine şikâyet yoluna gidilir.</li>
          </ul>
          <p>Bu süreler hak düşürücüdür; süre geçtikten sonra yapılan itirazlar dikkate alınmaz ve takip kesinleşir.</p>

          <h2>İcra takibi nasıl işler?</h2>
          <ol>
            <li><strong>Takip talebi:</strong> Alacaklı, icra dairesine takip talebinde bulunur.</li>
            <li><strong>Ödeme emri:</strong> Borçluya ödeme emri tebliğ edilir.</li>
            <li><strong>İtiraz veya kesinleşme:</strong> Süresinde itiraz edilmezse takip kesinleşir; itiraz edilirse takip durur.</li>
            <li><strong>Haciz:</strong> Kesinleşen takipte borçlunun mal, hak ve alacakları haczedilebilir.</li>
            <li><strong>Satış ve paraya çevirme:</strong> Haczedilen mallar satılarak alacak tahsil edilir.</li>
          </ol>

          <h2>Malatya'da icra işlemleri nereye yapılır?</h2>
          <p>Takipler icra dairelerinde yürütülür; şikâyet, itirazın kaldırılması ve kambiyo senetlerine dayalı takiplere itiraz gibi başvurular <strong>icra hukuk mahkemesinde</strong> incelenir. İtirazın iptali ve menfi tespit gibi davalar ise genel mahkemelerde görülür.</p>
""",
    "sss": [
      ("Ödeme emrine itiraz etmezsem ne olur?",
       "Süresinde itiraz edilmeyen takip kesinleşir ve alacaklı haciz isteyebilir. Borcun bulunmadığını sonradan ileri sürmek için menfi tespit veya istirdat davası gibi daha uzun ve masraflı yollara başvurmak gerekebilir."),
      ("Maaşın ne kadarı haczedilebilir?",
       "Nafaka alacakları dışında, borçlunun maaşının kural olarak dörtte birinden az olmamak üzere bir kısmı haczedilebilir. Haczedilemeyecek mal ve haklar İcra ve İflas Kanunu m. 82 ve 83'te sayılmıştır."),
      ("Çek veya senet nedeniyle takip başlatıldı, ne yapmalıyım?",
       "Kambiyo senetlerine dayalı takipte itiraz süresi beş gündür ve itiraz icra dairesine değil icra mahkemesine yapılır. Senetteki imza size ait değilse bunu ayrıca ve açıkça belirtmeniz gerekir."),
      ("İcra takibinde zamanaşımı var mıdır?",
       "Takip işlemsiz bırakıldığında, alacağın türüne göre zamanaşımı işlemeye devam edebilir. Zamanaşımı itirazı, takip türüne göre icra dairesine veya icra mahkemesine yapılır."),
    ],
  },
  {
    "slug": "malatya-gayrimenkul-avukati.html",
    "kisa": "Gayrimenkul Hukuku",
    "kategori": "Gayrimenkul Hukuku",
    "title": "Malatya Gayrimenkul Avukatı | Tapu ve Kira | Gelegen Hukuk Bürosu",
    "desc": "Malatya'da tapu iptali ve tescil, ortaklığın giderilmesi, kira tespit ve tahliye, kat karşılığı inşaat ve önalım davaları hakkında bilgi. Gelegen Hukuk Bürosu.",
    "h1": "Malatya Gayrimenkul Avukatı",
    "lead": "Taşınmaz uyuşmazlıkları çoğu zaman yüksek değerli ve uzun soluklu süreçlerdir. Tapu, kira, ortaklık ve inşaat sözleşmelerinden doğan davalarda bilmeniz gereken temel noktaları bu sayfada özetledik.",
    "kart": "Tapu iptali ve tescil, ortaklığın giderilmesi, kira tespit ve tahliye, kat karşılığı inşaat sözleşmeleri.",
    "body": """
          <h2>Gayrimenkul hukukunda hangi konularda destek veriyoruz?</h2>
          <ul>
            <li><strong>Tapu iptali ve tescil:</strong> Muris muvazaası, vekâletin kötüye kullanılması ve yolsuz tescil davaları.</li>
            <li><strong>Ortaklığın giderilmesi (izale-i şuyu):</strong> Hisseli taşınmazların aynen taksimi veya satış yoluyla paylaştırılması.</li>
            <li><strong>Kira uyuşmazlıkları:</strong> Kira bedelinin tespiti, tahliye ve kira alacağı davaları.</li>
            <li><strong>Kat karşılığı inşaat sözleşmeleri:</strong> Sözleşmenin hazırlanması, gecikme ve ayıp nedeniyle uyuşmazlıklar.</li>
            <li><strong>Önalım (şufa) hakkı</strong> ve elatmanın önlenmesi (müdahalenin meni) davaları.</li>
            <li><strong>Kat mülkiyeti</strong> uyuşmazlıkları ve kamulaştırma bedeline ilişkin davalar.</li>
          </ul>

          <h2>Zorunlu arabuluculuk kapsamındaki taşınmaz davaları</h2>
          <p>1 Eylül 2023 tarihinden itibaren kira ilişkisinden doğan uyuşmazlıklar, taşınmazların ortaklığının giderilmesi, kat mülkiyeti ve komşu hukukundan kaynaklanan uyuşmazlıklarda dava açmadan önce <strong>arabulucuya başvurmak zorunludur</strong>. İcra yoluyla tahliye talepleri bu kuralın dışında kalır.</p>

          <h2>Taşınmaz davalarında yetkili mahkeme</h2>
          <p>Taşınmaz üzerindeki ayni haklara ilişkin davalar, kesin yetki kuralı gereği <strong>taşınmazın bulunduğu yer mahkemesinde</strong> açılır. Malatya'daki bir taşınmaza ilişkin tapu iptali, ortaklığın giderilmesi veya elatmanın önlenmesi davası, davacı başka bir ilde yaşasa bile Malatya'da görülür. Kira ve ortaklığın giderilmesi davalarına sulh hukuk mahkemesi, tapu iptali ve tescil davalarına kural olarak asliye hukuk mahkemesi bakar.</p>

          <h2>Önemli süreler</h2>
          <ul>
            <li><strong>Önalım hakkı:</strong> Satışın hak sahibine bildirilmesinden itibaren <strong>üç ay</strong>, her hâlde satıştan itibaren <strong>iki yıl</strong> içinde kullanılmalıdır (TMK m. 733).</li>
            <li><strong>Kira tespit davası:</strong> Yeni dönemden en az otuz gün önce açılması veya kiracıya yazılı bildirim yapılması hâlinde yeni dönemin başından itibaren geçerli olur.</li>
          </ul>
""",
    "sss": [
      ("Hisseli tapuda diğer ortaklar satışa razı olmazsa ne yapılır?",
       "Paydaşlardan her biri ortaklığın giderilmesini isteyebilir. Mahkeme önce aynen taksim imkânını değerlendirir; mümkün değilse taşınmazın açık artırmayla satışına ve bedelin paylar oranında dağıtılmasına karar verir."),
      ("Muris muvazaası nedir?",
       "Miras bırakanın, mirasçılarından mal kaçırmak amacıyla gerçekte bağışladığı bir taşınmazı tapuda satış gibi göstermesidir. Mirasçılar bu durumda tapu iptali ve tescil davası açabilir."),
      ("Kiracıyı hangi durumlarda tahliye edebilirim?",
       "Konut veya işyeri ihtiyacı, yeniden inşa, kiracının yazılı tahliye taahhüdü, kira süresi içinde iki haklı ihtar ve kira bedelinin ödenmemesi gibi kanunda sayılan sebeplerle tahliye istenebilir. Her sebebin kendine özgü süre şartları vardır."),
      ("Taşınmaz davalarında harç nasıl hesaplanır?",
       "Tapu iptali ve ortaklığın giderilmesi gibi davalarda harç ve masraflar çoğunlukla taşınmazın değeri esas alınarak hesaplanır. Dava açmadan önce değer tespiti ve masraf öngörüsü yapılması önerilir."),
    ],
  },
  {
    "slug": "malatya-miras-avukati.html",
    "kisa": "Miras Hukuku",
    "kategori": "Miras Hukuku",
    "title": "Malatya Miras Avukatı | Miras Hukuku | Gelegen Hukuk Bürosu",
    "desc": "Malatya'da mirasçılık belgesi, mirasın reddi, tenkis, saklı pay, vasiyetname ve muris muvazaası davaları hakkında bilgi. Gelegen Hukuk Bürosu, Malatya.",
    "h1": "Malatya Miras Avukatı ve Miras Hukuku",
    "lead": "Bir yakının vefatının ardından mirasçıların hakları, borçlar ve mal paylaşımı belirli sürelere bağlı hukuki işlemler gerektirir. Miras hukukuna ilişkin temel bilgileri ve dikkat edilmesi gereken süreleri bu sayfada bulabilirsiniz.",
    "kart": "Mirasçılık belgesi, mirasın reddi, tenkis ve muris muvazaası davaları, vasiyetname düzenlenmesi.",
    "body": """
          <h2>Miras hukukunda hangi konularda destek veriyoruz?</h2>
          <ul>
            <li><strong>Mirasçılık belgesi (veraset ilamı)</strong> alınması.</li>
            <li><strong>Mirasın reddi</strong> ve borca batık terekenin hükmen reddi davaları.</li>
            <li><strong>Tenkis davaları:</strong> Saklı payı zedelenen mirasçıların hakkını koruma.</li>
            <li><strong>Muris muvazaası</strong> nedeniyle tapu iptali ve tescil davaları.</li>
            <li><strong>Vasiyetname</strong> düzenlenmesi, açılması ve vasiyetnamenin iptali davaları.</li>
            <li><strong>Terekenin paylaştırılması</strong> ve ortaklığın giderilmesi.</li>
          </ul>

          <h2>Saklı pay nedir?</h2>
          <p>Miras bırakan, mal varlığının tamamı üzerinde dilediği gibi tasarruf edemez; kanun bazı mirasçılara dokunulamayan bir pay tanır. Türk Medeni Kanunu m. 506'ya göre saklı pay oranları:</p>
          <ul>
            <li><strong>Altsoy (çocuklar, torunlar):</strong> Yasal miras payının yarısı,</li>
            <li><strong>Anne ve babadan her biri:</strong> Yasal miras payının dörtte biri,</li>
            <li><strong>Sağ kalan eş:</strong> Altsoy veya anne-baba ile birlikte mirasçı olursa yasal payının tamamı, diğer hâllerde dörtte üçü.</li>
          </ul>
          <p>Kardeşlerin saklı payı bulunmamaktadır. Saklı payı zedelenen mirasçı <strong>tenkis davası</strong> açabilir.</p>

          <h2>Miras hukukunda kritik süreler</h2>
          <ul>
            <li><strong>Mirasın reddi:</strong> Yasal mirasçılar için miras bırakanın ölümünü öğrenmeden itibaren <strong>üç ay</strong> (TMK m. 606).</li>
            <li><strong>Tenkis davası:</strong> Saklı payın zedelendiğinin öğrenilmesinden itibaren <strong>bir yıl</strong>, her hâlde vasiyetnamelerde açılma tarihinden, diğer tasarruflarda mirasın açılmasından itibaren <strong>on yıl</strong>.</li>
            <li><strong>Vasiyetnamenin iptali:</strong> İptal sebebinin ve mirasçı olduğunun öğrenilmesinden itibaren <strong>bir yıl</strong>, her hâlde vasiyetnamenin açılmasından itibaren <strong>on yıl</strong>.</li>
          </ul>

          <h2>Miras davaları nerede açılır?</h2>
          <p>Mirasın paylaşımına ve mirasçılık belgesinin iptaline ilişkin davalar, kural olarak <strong>miras bırakanın son yerleşim yeri</strong> mahkemesinde açılır. Mirasçılık belgesi sulh hukuk mahkemesinden veya noterden alınabilir. Taşınmazlara ilişkin tapu iptali davaları ise taşınmazın bulunduğu yerde görülür.</p>
""",
    "sss": [
      ("Mirasçılık belgesi nereden alınır?",
       "Mirasçılık belgesi, mirasçılardan birinin başvurusuyla herhangi bir noterden veya sulh hukuk mahkemesinden alınabilir. Yabancılık unsuru taşıyan durumlarda mahkemeye başvurmak gerekebilir."),
      ("Borçlu ölen yakınımın mirasını reddetmezsem borçlardan sorumlu olur muyum?",
       "Mirası kabul eden mirasçılar, terekenin borçlarından kural olarak kişisel olarak sorumlu olur. Bu nedenle borçlu bir miras söz konusuysa üç aylık ret süresi içinde hareket etmek önemlidir."),
      ("Babam malını tek bir çocuğuna bıraktı, ne yapabilirim?",
       "Bu tasarruf saklı payınızı zedeliyorsa tenkis davası açabilirsiniz. Tasarruf gerçekte bağış olduğu hâlde satış gibi gösterildiyse muris muvazaası nedeniyle tapu iptali davası da gündeme gelebilir."),
      ("Vasiyetname nasıl yapılır?",
       "Vasiyetname resmî şekilde (noter veya sulh hâkimi önünde), el yazısıyla ya da olağanüstü hâllerde sözlü olarak yapılabilir. Şekil şartlarına uyulmaması iptal sebebi olabileceğinden düzenleme aşamasında dikkat gerekir."),
    ],
  },
  {
    "slug": "malatya-ticaret-hukuku-avukati.html",
    "kisa": "Ticaret ve Şirketler Hukuku",
    "kategori": "Ticaret Hukuku",
    "title": "Malatya Ticaret Hukuku Avukatı | Şirketler Hukuku | Gelegen Hukuk Bürosu",
    "desc": "Malatya'da şirket kuruluşu, pay devri, genel kurul, ticari sözleşmeler, ticari alacaklar ve zorunlu arabuluculuk hakkında bilgi. Gelegen Hukuk Bürosu.",
    "h1": "Malatya Ticaret ve Şirketler Hukuku Avukatı",
    "lead": "Şirketlerin günlük işleyişinde doğru kurulan sözleşmeler ve zamanında alınan hukuki destek, uyuşmazlıkları çoğu zaman doğmadan önler. Ticaret ve şirketler hukukuna ilişkin temel bilgileri bu sayfada özetledik.",
    "kart": "Şirket kuruluşu, pay devri, genel kurul süreçleri, ticari sözleşmeler ve ticari uyuşmazlıklar.",
    "body": """
          <h2>Ticaret hukukunda hangi konularda destek veriyoruz?</h2>
          <ul>
            <li><strong>Şirket kuruluşu:</strong> Limited ve anonim şirket esas sözleşmelerinin hazırlanması ve tescil süreçleri.</li>
            <li><strong>Pay devri ve ortaklık yapısı:</strong> Pay devir sözleşmeleri, ortaklar arası sözleşmeler.</li>
            <li><strong>Genel kurul süreçleri</strong> ve genel kurul kararlarının iptali davaları.</li>
            <li><strong>Ticari sözleşmeler:</strong> Satış, bayilik, distribütörlük, kira ve hizmet sözleşmelerinin hazırlanması ve incelenmesi.</li>
            <li><strong>Ticari alacak davaları</strong> ve haksız rekabet uyuşmazlıkları.</li>
            <li><strong>Sürekli hukuki danışmanlık:</strong> Şirketlerin günlük hukuki işlemlerinde destek.</li>
          </ul>

          <h2>Ticari davalarda zorunlu arabuluculuk</h2>
          <p>Konusu bir miktar paranın ödenmesi olan alacak ve tazminat talepleri hakkındaki ticari davalarda, dava açılmadan önce <strong>arabulucuya başvurulması dava şartıdır</strong> (Türk Ticaret Kanunu m. 5/A). Arabuluculuk aşamasında anlaşma sağlanırsa uyuşmazlık mahkemeye taşınmadan sona erer.</p>

          <h2>Genel kurul kararlarına itiraz</h2>
          <p>Kanun veya esas sözleşme hükümlerine ya da dürüstlük kuralına aykırı genel kurul kararlarının iptali, karar tarihinden itibaren <strong>üç ay</strong> içinde şirket merkezinin bulunduğu yerdeki asliye ticaret mahkemesinde dava açılarak istenebilir (TTK m. 445). Bu süre hak düşürücüdür.</p>

          <h2>Ticari davalar hangi mahkemede görülür?</h2>
          <p>Ticari davalara <strong>asliye ticaret mahkemesi</strong> bakar; asliye ticaret mahkemesi bulunmayan yerlerde asliye hukuk mahkemesi bu sıfatla görev yapar. Ticari defterler ve kayıtlar, bu davalarda önemli bir delil kaynağıdır; kayıtların düzenli tutulması uyuşmazlık hâlinde ispatı kolaylaştırır.</p>
""",
    "sss": [
      ("Limited şirkette pay devri nasıl yapılır?",
       "Limited şirket payının devri, yazılı şekilde yapılması ve imzaların noterce onaylanması gereken bir sözleşmeyle gerçekleşir. Esas sözleşmede aksi öngörülmedikçe devrin geçerli olması için genel kurulun onayı da gerekir."),
      ("Ticari bir alacak için doğrudan dava açabilir miyim?",
       "Konusu para alacağı olan ticari davalarda önce arabulucuya başvurmak zorunludur. Alternatif olarak, koşulları varsa icra takibi yoluna da gidilebilir."),
      ("Şirket ortağı olarak sorumluluğum nedir?",
       "Limited ve anonim şirketlerde ortakların sorumluluğu kural olarak taahhüt ettikleri sermaye ile sınırlıdır. Ancak limited şirket ortaklarının, tahsil edilemeyen kamu alacaklarından payları oranında sorumluluğu gibi özel düzenlemeler bulunmaktadır."),
    ],
  },
  {
    "slug": "malatya-idare-hukuku-avukati.html",
    "kisa": "İdare ve Vergi Hukuku",
    "kategori": "İdare Hukuku",
    "title": "Malatya İdare Hukuku Avukatı | İptal ve Tam Yargı | Gelegen Hukuk Bürosu",
    "desc": "Malatya'da iptal ve tam yargı davaları, idari para cezalarına itiraz, kamulaştırma ve vergi uyuşmazlıkları hakkında bilgi. Gelegen Hukuk Bürosu, Malatya.",
    "h1": "Malatya İdare ve Vergi Hukuku Avukatı",
    "lead": "Kamu kurumlarının işlem ve eylemlerine karşı başvuru yolları kısa sürelere bağlıdır ve doğru mercinin seçilmesi büyük önem taşır. İdare ve vergi hukukuna ilişkin temel bilgileri bu sayfada bulabilirsiniz.",
    "kart": "İptal ve tam yargı davaları, idari para cezalarına itiraz, kamulaştırma ve vergi uyuşmazlıkları.",
    "body": """
          <h2>İdare hukukunda hangi konularda destek veriyoruz?</h2>
          <ul>
            <li><strong>İptal davaları:</strong> Hukuka aykırı idari işlemlerin (atama, disiplin cezası, ruhsat iptali vb.) iptali.</li>
            <li><strong>Tam yargı davaları:</strong> İdarenin işlem veya eylemlerinden doğan zararların tazmini.</li>
            <li><strong>İdari para cezalarına itiraz</strong> (trafik cezaları dahil).</li>
            <li><strong>Kamulaştırma:</strong> Kamulaştırma bedelinin tespiti ve kamulaştırmasız el atma davaları.</li>
            <li><strong>Vergi uyuşmazlıkları:</strong> Vergi ve ceza ihbarnamelerine karşı uzlaşma ve dava süreçleri.</li>
            <li><strong>İmar uygulamaları</strong> ve yıkım kararlarına karşı başvurular.</li>
          </ul>

          <h2>İdari davalarda dava açma süreleri</h2>
          <ul>
            <li><strong>İdare mahkemelerinde:</strong> Özel kanunlarda ayrı süre gösterilmeyen hâllerde <strong>60 gün</strong> (İdari Yargılama Usulü Kanunu m. 7).</li>
            <li><strong>Vergi mahkemelerinde:</strong> <strong>30 gün</strong>.</li>
            <li><strong>İdari para cezalarına itiraz:</strong> Kararın tebliğinden veya öğrenilmesinden itibaren <strong>15 gün</strong> içinde sulh ceza hâkimliğine (Kabahatler Kanunu m. 27).</li>
          </ul>
          <p>Süreler, işlemin ilgiliye yazılı bildiriminden itibaren işlemeye başlar. Süre geçtikten sonra açılan dava, esasa girilmeden reddedilir.</p>

          <h2>İdareye başvuru ve zımni ret</h2>
          <p>Bir işlemin yapılması için idareye başvurulduğunda idare <strong>30 gün</strong> içinde cevap vermezse istek reddedilmiş sayılır. Bu durumda, sürenin bitiminden itibaren dava açma süresi içinde idari yargıya başvurulabilir (İYUK m. 10).</p>

          <h2>Malatya'da idari davalar nerede görülür?</h2>
          <p>Malatya'daki idari işlemlere karşı açılan davalar <strong>Malatya İdare Mahkemesi</strong> ve <strong>Malatya Vergi Mahkemesinde</strong> görülür. Kural olarak yetkili mahkeme, işlemi yapan idari merciin bulunduğu yer mahkemesidir; kamu görevlilerine ilişkin bazı uyuşmazlıklarda ise görev yeri esas alınır.</p>
""",
    "sss": [
      ("Trafik cezasına nasıl itiraz edilir?",
       "Trafik idari para cezalarına, tebliğ tarihinden itibaren 15 gün içinde sulh ceza hâkimliğine başvurularak itiraz edilir. Cezanın erken ödeme indirimiyle ödenmiş olması itiraz hakkını ortadan kaldırmaz."),
      ("İdari işlemin uygulanmasını durdurabilir miyim?",
       "İptal davası açılırken yürütmenin durdurulması talep edilebilir. Mahkeme, işlemin açıkça hukuka aykırı olması ve uygulanması hâlinde telafisi güç veya imkânsız zararların doğması şartlarının birlikte gerçekleştiğini görürse yürütmeyi durdurur."),
      ("Arazime kamulaştırmasız el atıldı, ne yapabilirim?",
       "İdarenin usulüne uygun kamulaştırma yapmadan taşınmaza fiilen el atması hâlinde bedelin ödenmesi veya el atmanın önlenmesi için dava açılabilir. Davada taşınmazın güncel değeri bilirkişi incelemesiyle belirlenir."),
    ],
  },
]
