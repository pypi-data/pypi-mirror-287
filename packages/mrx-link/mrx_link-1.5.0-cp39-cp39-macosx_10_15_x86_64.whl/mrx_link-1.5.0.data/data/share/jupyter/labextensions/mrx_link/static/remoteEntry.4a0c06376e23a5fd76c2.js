var _JUPYTERLAB;(()=>{"use strict";var e,t,a,r,n,o,l,f,d,i,c,u,s,b,h,p,m,v,g,y,j,P,w,x,k,S={2012:(e,t,a)=>{var r={"./index":()=>Promise.all([a.e(384),a.e(725),a.e(632),a.e(893),a.e(520),a.e(598),a.e(567),a.e(475)]).then((()=>()=>a(93726))),"./extension":()=>Promise.all([a.e(384),a.e(725),a.e(632),a.e(893),a.e(520),a.e(598),a.e(567),a.e(475)]).then((()=>()=>a(93726))),"./style":()=>a.e(331).then((()=>()=>a(87331)))},n=(e,t)=>(a.R=t,t=a.o(r,e)?r[e]():Promise.resolve().then((()=>{throw new Error('Module "'+e+'" does not exist in container.')})),a.R=void 0,t),o=(e,t)=>{if(a.S){var r="default",n=a.S[r];if(n&&n!==e)throw new Error("Container initialization failed as it has already been initialized with a different share scope");return a.S[r]=e,a.I(r,t)}};a.d(t,{get:()=>n,init:()=>o})}},E={};function _(e){var t=E[e];if(void 0!==t)return t.exports;var a=E[e]={id:e,loaded:!1,exports:{}};return S[e].call(a.exports,a,a.exports,_),a.loaded=!0,a.exports}_.m=S,_.c=E,_.amdD=function(){throw new Error("define cannot be used indirect")},_.n=e=>{var t=e&&e.__esModule?()=>e.default:()=>e;return _.d(t,{a:t}),t},_.d=(e,t)=>{for(var a in t)_.o(t,a)&&!_.o(e,a)&&Object.defineProperty(e,a,{enumerable:!0,get:t[a]})},_.f={},_.e=e=>Promise.all(Object.keys(_.f).reduce(((t,a)=>(_.f[a](e,t),t)),[])),_.u=e=>e+"."+{108:"06a6acbc38069ad07123",109:"aad1652a34b9705ab6df",213:"432fd8200b0b707a9a56",246:"9d4c075b73118249d39b",262:"ed92dfbbc04760422c40",285:"da515649078e6ae2b5f6",292:"267b5ecaf80bffbbbf08",331:"a20b4f16d245db313a2b",344:"cd6bd7ba074fb6198da7",384:"19dcfe3e5320229d0194",474:"94608ea2305ca6d849f1",475:"c1c54fc73f62e7461f0b",490:"c8ab6b46c8b068c2f08f",505:"3daae60b184d3734f00d",520:"eb187771f718574fe62b",543:"871a5a58517d871167d9",567:"c4182eba88b7e4bfd41c",598:"aec005ae66fc72469799",606:"83ab9ba762db0e4a340c",632:"614da95604306fda2ac1",695:"a2fe5e45f7ad11aa2b13",708:"776a7a85b37df35be816",725:"c714f36737855fe60e72",727:"0f927c143b3d9f037035",743:"350fc36a1b501a3ede61",744:"a7d74d317fcc525f492b",813:"51213eb2d29498b51295",819:"1fc63504c15f3ed6fd31",868:"e55f2897557f00d7234e",871:"3bfc51e62cbfae7db811",881:"7a9e2483a7832f8e2920",893:"f79f5c290d2d60509d62",901:"166751d2de07fbb7cd57",911:"65c00c4b2e989a2991db",959:"5419816a3d852933994e"}[e]+".js?v="+{108:"06a6acbc38069ad07123",109:"aad1652a34b9705ab6df",213:"432fd8200b0b707a9a56",246:"9d4c075b73118249d39b",262:"ed92dfbbc04760422c40",285:"da515649078e6ae2b5f6",292:"267b5ecaf80bffbbbf08",331:"a20b4f16d245db313a2b",344:"cd6bd7ba074fb6198da7",384:"19dcfe3e5320229d0194",474:"94608ea2305ca6d849f1",475:"c1c54fc73f62e7461f0b",490:"c8ab6b46c8b068c2f08f",505:"3daae60b184d3734f00d",520:"eb187771f718574fe62b",543:"871a5a58517d871167d9",567:"c4182eba88b7e4bfd41c",598:"aec005ae66fc72469799",606:"83ab9ba762db0e4a340c",632:"614da95604306fda2ac1",695:"a2fe5e45f7ad11aa2b13",708:"776a7a85b37df35be816",725:"c714f36737855fe60e72",727:"0f927c143b3d9f037035",743:"350fc36a1b501a3ede61",744:"a7d74d317fcc525f492b",813:"51213eb2d29498b51295",819:"1fc63504c15f3ed6fd31",868:"e55f2897557f00d7234e",871:"3bfc51e62cbfae7db811",881:"7a9e2483a7832f8e2920",893:"f79f5c290d2d60509d62",901:"166751d2de07fbb7cd57",911:"65c00c4b2e989a2991db",959:"5419816a3d852933994e"}[e],_.g=function(){if("object"==typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"==typeof window)return window}}(),_.o=(e,t)=>Object.prototype.hasOwnProperty.call(e,t),e={},t="mrx_link:",_.l=(a,r,n,o)=>{if(e[a])e[a].push(r);else{var l,f;if(void 0!==n)for(var d=document.getElementsByTagName("script"),i=0;i<d.length;i++){var c=d[i];if(c.getAttribute("src")==a||c.getAttribute("data-webpack")==t+n){l=c;break}}l||(f=!0,(l=document.createElement("script")).charset="utf-8",l.timeout=120,_.nc&&l.setAttribute("nonce",_.nc),l.setAttribute("data-webpack",t+n),l.src=a),e[a]=[r];var u=(t,r)=>{l.onerror=l.onload=null,clearTimeout(s);var n=e[a];if(delete e[a],l.parentNode&&l.parentNode.removeChild(l),n&&n.forEach((e=>e(r))),t)return t(r)},s=setTimeout(u.bind(null,void 0,{type:"timeout",target:l}),12e4);l.onerror=u.bind(null,l.onerror),l.onload=u.bind(null,l.onload),f&&document.head.appendChild(l)}},_.r=e=>{"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},_.nmd=e=>(e.paths=[],e.children||(e.children=[]),e),(()=>{_.S={};var e={},t={};_.I=(a,r)=>{r||(r=[]);var n=t[a];if(n||(n=t[a]={}),!(r.indexOf(n)>=0)){if(r.push(n),e[a])return e[a];_.o(_.S,a)||(_.S[a]={});var o=_.S[a],l="mrx_link",f=(e,t,a,r)=>{var n=o[e]=o[e]||{},f=n[t];(!f||!f.loaded&&(!r!=!f.eager?r:l>f.from))&&(n[t]={get:a,from:l,eager:!!r})},d=[];return"default"===a&&(f("@dagrejs/graphlib","2.2.2",(()=>_.e(743).then((()=>()=>_(96743))))),f("@emotion/react","11.11.4",(()=>Promise.all([_.e(384),_.e(871),_.e(893),_.e(344)]).then((()=>()=>_(78871))))),f("@emotion/styled","11.11.5",(()=>Promise.all([_.e(868),_.e(893),_.e(598),_.e(744),_.e(285)]).then((()=>()=>_(1868))))),f("@mui/material","5.15.15",(()=>Promise.all([_.e(384),_.e(695),_.e(725),_.e(893),_.e(520),_.e(598),_.e(567)]).then((()=>()=>_(68695))))),f("@preact/signals","1.2.3",(()=>_.e(292).then((()=>()=>_(18911))))),f("axios","0.24.0",(()=>Promise.all([_.e(505),_.e(606)]).then((()=>()=>_(72505))))),f("d3","7.9.0",(()=>_.e(819).then((()=>()=>_(47819))))),f("dagre","0.8.5",(()=>_.e(246).then((()=>()=>_(76246))))),f("file-saver","2.0.5",(()=>_.e(213).then((()=>()=>_(4213))))),f("lodash","4.17.21",(()=>_.e(543).then((()=>()=>_(2543))))),f("mobx-react-lite","3.4.3",(()=>Promise.all([_.e(893),_.e(520),_.e(474),_.e(881)]).then((()=>()=>_(2881))))),f("mobx","6.12.3",(()=>_.e(813).then((()=>()=>_(27813))))),f("mrx_link","1.5.0",(()=>Promise.all([_.e(384),_.e(725),_.e(632),_.e(893),_.e(520),_.e(598),_.e(567),_.e(475)]).then((()=>()=>_(93726))))),f("plotly.js-dist-min","2.32.0",(()=>_.e(708).then((()=>()=>_(84708))))),f("react-colorful","5.6.1",(()=>Promise.all([_.e(893),_.e(109)]).then((()=>()=>_(38109))))),f("react-sortablejs","6.1.4",(()=>Promise.all([_.e(901),_.e(893)]).then((()=>()=>_(15901))))),f("toastr","2.1.4",(()=>_.e(959).then((()=>()=>_(47959)))))),e[a]=d.length?Promise.all(d).then((()=>e[a]=1)):1}}})(),(()=>{var e;_.g.importScripts&&(e=_.g.location+"");var t=_.g.document;if(!e&&t&&(t.currentScript&&(e=t.currentScript.src),!e)){var a=t.getElementsByTagName("script");if(a.length)for(var r=a.length-1;r>-1&&(!e||!/^http(s?):/.test(e));)e=a[r--].src}if(!e)throw new Error("Automatic publicPath is not supported in this browser");e=e.replace(/#.*$/,"").replace(/\?.*$/,"").replace(/\/[^\/]+$/,"/"),_.p=e})(),a=e=>{var t=e=>e.split(".").map((e=>+e==e?+e:e)),a=/^([^-+]+)?(?:-([^+]+))?(?:\+(.+))?$/.exec(e),r=a[1]?t(a[1]):[];return a[2]&&(r.length++,r.push.apply(r,t(a[2]))),a[3]&&(r.push([]),r.push.apply(r,t(a[3]))),r},r=(e,t)=>{e=a(e),t=a(t);for(var r=0;;){if(r>=e.length)return r<t.length&&"u"!=(typeof t[r])[0];var n=e[r],o=(typeof n)[0];if(r>=t.length)return"u"==o;var l=t[r],f=(typeof l)[0];if(o!=f)return"o"==o&&"n"==f||"s"==f||"u"==o;if("o"!=o&&"u"!=o&&n!=l)return n<l;r++}},n=e=>{var t=e[0],a="";if(1===e.length)return"*";if(t+.5){a+=0==t?">=":-1==t?"<":1==t?"^":2==t?"~":t>0?"=":"!=";for(var r=1,o=1;o<e.length;o++)r--,a+="u"==(typeof(f=e[o]))[0]?"-":(r>0?".":"")+(r=2,f);return a}var l=[];for(o=1;o<e.length;o++){var f=e[o];l.push(0===f?"not("+d()+")":1===f?"("+d()+" || "+d()+")":2===f?l.pop()+" "+l.pop():n(f))}return d();function d(){return l.pop().replace(/^\((.+)\)$/,"$1")}},o=(e,t)=>{if(0 in e){t=a(t);var r=e[0],n=r<0;n&&(r=-r-1);for(var l=0,f=1,d=!0;;f++,l++){var i,c,u=f<e.length?(typeof e[f])[0]:"";if(l>=t.length||"o"==(c=(typeof(i=t[l]))[0]))return!d||("u"==u?f>r&&!n:""==u!=n);if("u"==c){if(!d||"u"!=u)return!1}else if(d)if(u==c)if(f<=r){if(i!=e[f])return!1}else{if(n?i>e[f]:i<e[f])return!1;i!=e[f]&&(d=!1)}else if("s"!=u&&"n"!=u){if(n||f<=r)return!1;d=!1,f--}else{if(f<=r||c<u!=n)return!1;d=!1}else"s"!=u&&"n"!=u&&(d=!1,f--)}}var s=[],b=s.pop.bind(s);for(l=1;l<e.length;l++){var h=e[l];s.push(1==h?b()|b():2==h?b()&b():h?o(h,t):!b())}return!!b()},l=(e,t)=>{var a=_.S[e];if(!a||!_.o(a,t))throw new Error("Shared module "+t+" doesn't exist in shared scope "+e);return a},f=(e,t)=>{var a=e[t];return(t=Object.keys(a).reduce(((e,t)=>!e||r(e,t)?t:e),0))&&a[t]},d=(e,t)=>{var a=e[t];return Object.keys(a).reduce(((e,t)=>!e||!a[e].loaded&&r(e,t)?t:e),0)},i=(e,t,a,r)=>"Unsatisfied version "+a+" from "+(a&&e[t][a].from)+" of shared singleton module "+t+" (required "+n(r)+")",c=(e,t,a,r)=>{var n=d(e,a);return o(r,n)||b(i(e,a,n,r)),p(e[a][n])},u=(e,t,a)=>{var n=e[t];return(t=Object.keys(n).reduce(((e,t)=>!o(a,t)||e&&!r(e,t)?e:t),0))&&n[t]},s=(e,t,a,r)=>{var o=e[a];return"No satisfying version ("+n(r)+") of shared module "+a+" found in shared scope "+t+".\nAvailable versions: "+Object.keys(o).map((e=>e+" from "+o[e].from)).join(", ")},b=e=>{"undefined"!=typeof console&&console.warn&&console.warn(e)},h=(e,t,a,r)=>{b(s(e,t,a,r))},p=e=>(e.loaded=1,e.get()),v=(m=e=>function(t,a,r,n){var o=_.I(t);return o&&o.then?o.then(e.bind(e,t,_.S[t],a,r,n)):e(t,_.S[t],a,r,n)})(((e,t,a,r)=>t&&_.o(t,a)?p(f(t,a)):r())),g=m(((e,t,a,r)=>(l(e,a),p(u(t,a,r)||h(t,e,a,r)||f(t,a))))),y=m(((e,t,a,r)=>(l(e,a),c(t,0,a,r)))),j=m(((e,t,a,r,n)=>{var o=t&&_.o(t,a)&&u(t,a,r);return o?p(o):n()})),P={},w={8893:()=>y("default","react",[1,17,0,1]),59520:()=>y("default","react-dom",[1,17,0,1]),81598:()=>v("default","@emotion/react",(()=>Promise.all([_.e(384),_.e(871),_.e(727)]).then((()=>()=>_(78871))))),9443:()=>j("default","@emotion/styled",[1,11,3,0],(()=>Promise.all([_.e(868),_.e(744)]).then((()=>()=>_(1868))))),83157:()=>j("default","@emotion/react",[1,11,4,1],(()=>Promise.all([_.e(871),_.e(108)]).then((()=>()=>_(78871))))),1041:()=>y("default","@jupyterlab/statusbar",[1,3,6,7]),1290:()=>y("default","@jupyterlab/mainmenu",[1,3,6,7]),3498:()=>y("default","@jupyterlab/filebrowser",[1,3,6,7]),4112:()=>y("default","@lumino/widgets",[1,1,37,2]),8483:()=>y("default","@lumino/coreutils",[1,1,11,0]),19604:()=>y("default","@jupyterlab/apputils",[1,3,6,7]),19740:()=>j("default","@emotion/react",[1,11,11,4],(()=>Promise.all([_.e(871),_.e(108)]).then((()=>()=>_(78871))))),21079:()=>j("default","lodash",[1,4,17,21],(()=>_.e(543).then((()=>()=>_(2543))))),30982:()=>j("default","dagre",[2,0,8,5],(()=>_.e(246).then((()=>()=>_(76246))))),34442:()=>j("default","mobx-react-lite",[1,3,4,3],(()=>Promise.all([_.e(474),_.e(262)]).then((()=>()=>_(2881))))),34835:()=>j("default","plotly.js-dist-min",[1,2,30,1],(()=>_.e(708).then((()=>()=>_(84708))))),38127:()=>g("default","@jupyterlab/outputarea",[1,3,6,7]),40813:()=>j("default","react-colorful",[1,5,6,1],(()=>_.e(490).then((()=>()=>_(38109))))),45214:()=>y("default","@jupyterlab/coreutils",[1,5,6,7]),53324:()=>j("default","@dagrejs/graphlib",[1,2,2,1],(()=>_.e(743).then((()=>()=>_(96743))))),66689:()=>j("default","@preact/signals",[1,1,2,3],(()=>_.e(911).then((()=>()=>_(18911))))),66840:()=>j("default","d3",[1,7,9,0],(()=>_.e(819).then((()=>()=>_(47819))))),70809:()=>y("default","@jupyterlab/statedb",[1,3,6,7]),75166:()=>y("default","@jupyterlab/application",[1,3,6,7]),76441:()=>j("default","react-sortablejs",[1,6,1,4],(()=>_.e(901).then((()=>()=>_(15901))))),78115:()=>j("default","@emotion/styled",[1,11,11,5],(()=>Promise.all([_.e(868),_.e(744)]).then((()=>()=>_(1868))))),79303:()=>y("default","@lumino/algorithm",[1,1,9,0]),80454:()=>y("default","@lumino/disposable",[1,1,10,0]),87271:()=>y("default","@jupyterlab/notebook",[1,3,6,7]),88034:()=>j("default","@mui/material",[1,5,15,15],(()=>_.e(695).then((()=>()=>_(68695))))),88416:()=>j("default","file-saver",[1,2,0,5],(()=>_.e(213).then((()=>()=>_(4213))))),89539:()=>j("default","mobx",[1,6,12,3],(()=>_.e(813).then((()=>()=>_(27813))))),90875:()=>j("default","axios",[2,0,24,0],(()=>_.e(505).then((()=>()=>_(72505))))),94644:()=>y("default","@lumino/signaling",[1,1,10,0]),95005:()=>j("default","toastr",[1,2,1,4],(()=>_.e(959).then((()=>()=>_(47959))))),95827:()=>y("default","@jupyterlab/ui-components",[1,3,6,7]),96603:()=>y("default","@jupyterlab/services",[1,6,6,7]),98234:()=>g("default","@jupyterlab/cells",[1,3,6,7]),52744:()=>j("default","@emotion/react",[1,11,0,0,,"rc",0],(()=>Promise.all([_.e(384),_.e(871)]).then((()=>()=>_(78871))))),52474:()=>j("default","mobx",[1,6,1,0],(()=>_.e(813).then((()=>()=>_(27813)))))},x={474:[52474],475:[1041,1290,3498,4112,8483,19604,19740,21079,30982,34442,34835,38127,40813,45214,53324,66689,66840,70809,75166,76441,78115,79303,80454,87271,88034,88416,89539,90875,94644,95005,95827,96603,98234],520:[59520],567:[9443,83157],598:[81598],744:[52744],893:[8893]},k={},_.f.consumes=(e,t)=>{_.o(x,e)&&x[e].forEach((e=>{if(_.o(P,e))return t.push(P[e]);if(!k[e]){var a=t=>{P[e]=0,_.m[e]=a=>{delete _.c[e],a.exports=t()}};k[e]=!0;var r=t=>{delete P[e],_.m[e]=a=>{throw delete _.c[e],t}};try{var n=w[e]();n.then?t.push(P[e]=n.then(a).catch(r)):a(n)}catch(e){r(e)}}}))},(()=>{var e={129:0};_.f.j=(t,a)=>{var r=_.o(e,t)?e[t]:void 0;if(0!==r)if(r)a.push(r[2]);else if(/^(5(20|67|98)|474|744|893)$/.test(t))e[t]=0;else{var n=new Promise(((a,n)=>r=e[t]=[a,n]));a.push(r[2]=n);var o=_.p+_.u(t),l=new Error;_.l(o,(a=>{if(_.o(e,t)&&(0!==(r=e[t])&&(e[t]=void 0),r)){var n=a&&("load"===a.type?"missing":a.type),o=a&&a.target&&a.target.src;l.message="Loading chunk "+t+" failed.\n("+n+": "+o+")",l.name="ChunkLoadError",l.type=n,l.request=o,r[1](l)}}),"chunk-"+t,t)}};var t=(t,a)=>{var r,n,[o,l,f]=a,d=0;if(o.some((t=>0!==e[t]))){for(r in l)_.o(l,r)&&(_.m[r]=l[r]);f&&f(_)}for(t&&t(a);d<o.length;d++)n=o[d],_.o(e,n)&&e[n]&&e[n][0](),e[n]=0},a=self.webpackChunkmrx_link=self.webpackChunkmrx_link||[];a.forEach(t.bind(null,0)),a.push=t.bind(null,a.push.bind(a))})(),_.nc=void 0;var T=_(2012);(_JUPYTERLAB=void 0===_JUPYTERLAB?{}:_JUPYTERLAB).mrx_link=T})();