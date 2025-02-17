true 
false 
Birinci için konuşursak a is b çıktısının True olmasının sebebi:
Python, -5 ile 256 arasındaki küçük tamsayıları belleğne alır . Yani, a = 256 ve b = 256 atandığında,
her ikisi de bellekte aynı nesneyi referans eder. Bu yüzden a is b ifadesi truye döner. 



c is d çıktısının False olmasının sebebi:
256'nın üzerindeki sayılar belleğe alınmaz. c = 257 ve d = 257 atandığında, 
Python bunlar için farklı bellek adreslerinde yeni nesneler oluşturur. Dolayısıyla c is d ifadesi False olur.   