l = ['charlie', 'bob', 'dave', 'bob']
l.remove('bob')
print(l)

l.append('bob')

l = [e for e in l if e not in ('bob', 'charlie')]
print(l)

product_prices = [<span style="font-size:0"></span>, <span class="">$<!-- -->59</span>, <span class="">$<!-- -->78</span>, <span class="">$<!-- -->39<span aria-label="to"> - </span>$<!-- -->69</span>, <span aria-label="to"> - </span>, <span class="">$<!-- -->88</span>, <span class="">$<!-- -->79</span>, <span class="">$<!-- -->128</span>, <span class="">$<!-- -->39</span>, <span class="">$<!-- -->64</span>, <span class="">$<!-- -->39<span aria-label="to"> - </span>$<!-- -->49</span>, <span aria-label="to"> - </span>, <span class="">$<!-- -->68</span>, <span class="">$<!-- -->84<span aria-label="to"> - </span>$<!-- -->89</span>, <span aria-label="to"> - </span>, <span class="">$<!-- -->118</span>, <span class="">$<!-- -->49</span>, <span class="">$<!-- -->68</span>, <span class="">$<!-- -->59<span aria-label="to"> - </span>$<!-- -->69</span>, <span aria-label="to"> - </span>, <span class="">$<!-- -->78</span>, <span class="">$<!-- -->84<span aria-label="to"> - </span>$<!-- -->99</span>, <span aria-label="to"> - </span>, <span class="">$<!-- -->128</span>, <span class="">$<!-- -->39<span aria-label="to"> - </span>$<!-- -->59</span>, <span aria-label="to"> - </span>, <span class="">$<!-- -->64<span aria-label="to"> - </span>$<!-- -->74</span>, <span aria-label="to"> - </span>, <span class="">$<!-- -->69</span>, <span class="">$<!-- -->88</span>, <span class="">$<!-- -->49</span>, <span class="">$<!-- -->68</span>, <span data-testid="bottom-script">
<script type="text/javascript">
        window.addEventListener('PEPS', function () {
          if (typeof _satellite !== 'undefined') {
            _satellite.track('window-onload');
          }
        });
        if (typeof _satellite !== 'undefined' && !window.dontLoadTarget) {
          _satellite.pageBottom();
        }
    </script>
<script>
     document.addEventListener('readystatechange', function () {
      if(document.readyState === 'loaded') {
      const scriptOee = document.createElement('script');
      scriptOee.async = true;
      scriptOee.onload = function() {
        ATGSvcs.setEEID("201902085120741");
        (function() {
          var l = 'lululemon.custhelp.com',d=document,ss='script',s=d.getElementsByTagName(ss)[0];
          function r(u) {
          var rn=d.createElement(ss);
          rn.type='text/javascript';
          rn.defer=rn.async=!0;
          rn.src = "//" + l + u;
          s.parentNode.insertBefore(rn,s);
          }
          r('/rnt/rnw/javascript/vs/1/vsapi.js');
          r('/vs/1/vsopts.js');
        })();
      }
      scriptOee.src = "https://static.atgsvcs.com/js/atgsvcs.js";
      document.head.appendChild(scriptOee);
           }
        });
    </script>
</span>
                  ]

for p in product_prices:
    print(p.text)