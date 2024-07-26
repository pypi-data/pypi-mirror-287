"use strict";(self.webpackChunkmrx_link=self.webpackChunkmrx_link||[]).push([[490,109],{38109:(e,r,t)=>{t.r(r),t.d(r,{HexAlphaColorPicker:()=>ee,HexColorInput:()=>ye,HexColorPicker:()=>Q,HslColorPicker:()=>le,HslStringColorPicker:()=>ce,HslaColorPicker:()=>te,HslaStringColorPicker:()=>oe,HsvColorPicker:()=>he,HsvStringColorPicker:()=>ge,HsvaColorPicker:()=>ie,HsvaStringColorPicker:()=>ve,RgbColorPicker:()=>He,RgbStringColorPicker:()=>ke,RgbaColorPicker:()=>be,RgbaStringColorPicker:()=>_e,setNonce:()=>Y});var n=t(8893),o=t.n(n);function a(){return(a=Object.assign||function(e){for(var r=1;r<arguments.length;r++){var t=arguments[r];for(var n in t)Object.prototype.hasOwnProperty.call(t,n)&&(e[n]=t[n])}return e}).apply(this,arguments)}function l(e,r){if(null==e)return{};var t,n,o={},a=Object.keys(e);for(n=0;n<a.length;n++)r.indexOf(t=a[n])>=0||(o[t]=e[t]);return o}function u(e){var r=(0,n.useRef)(e),t=(0,n.useRef)((function(e){r.current&&r.current(e)}));return r.current=e,t.current}var c=function(e,r,t){return void 0===r&&(r=0),void 0===t&&(t=1),e>t?t:e<r?r:e},s=function(e){return"touches"in e},i=function(e){return e&&e.ownerDocument.defaultView||self},f=function(e,r,t){var n=e.getBoundingClientRect(),o=s(r)?function(e,r){for(var t=0;t<e.length;t++)if(e[t].identifier===r)return e[t];return e[0]}(r.touches,t):r;return{left:c((o.pageX-(n.left+i(e).pageXOffset))/n.width),top:c((o.pageY-(n.top+i(e).pageYOffset))/n.height)}},v=function(e){!s(e)&&e.preventDefault()},d=o().memo((function(e){var r=e.onMove,t=e.onKey,c=l(e,["onMove","onKey"]),d=(0,n.useRef)(null),h=u(r),m=u(t),g=(0,n.useRef)(null),p=(0,n.useRef)(!1),b=(0,n.useMemo)((function(){var e=function(e){v(e),(s(e)?e.touches.length>0:e.buttons>0)&&d.current?h(f(d.current,e,g.current)):t(!1)},r=function(){return t(!1)};function t(t){var n=p.current,o=i(d.current),a=t?o.addEventListener:o.removeEventListener;a(n?"touchmove":"mousemove",e),a(n?"touchend":"mouseup",r)}return[function(e){var r=e.nativeEvent,n=d.current;if(n&&(v(r),!function(e,r){return r&&!s(e)}(r,p.current)&&n)){if(s(r)){p.current=!0;var o=r.changedTouches||[];o.length&&(g.current=o[0].identifier)}n.focus(),h(f(n,r,g.current)),t(!0)}},function(e){var r=e.which||e.keyCode;r<37||r>40||(e.preventDefault(),m({left:39===r?.05:37===r?-.05:0,top:40===r?.05:38===r?-.05:0}))},t]}),[m,h]),C=b[0],_=b[1],E=b[2];return(0,n.useEffect)((function(){return E}),[E]),o().createElement("div",a({},c,{onTouchStart:C,onMouseDown:C,className:"react-colorful__interactive",ref:d,onKeyDown:_,tabIndex:0,role:"slider"}))})),h=function(e){return e.filter(Boolean).join(" ")},m=function(e){var r=e.color,t=e.left,n=e.top,a=void 0===n?.5:n,l=h(["react-colorful__pointer",e.className]);return o().createElement("div",{className:l,style:{top:100*a+"%",left:100*t+"%"}},o().createElement("div",{className:"react-colorful__pointer-fill",style:{backgroundColor:r}}))},g=function(e,r,t){return void 0===r&&(r=0),void 0===t&&(t=Math.pow(10,r)),Math.round(t*e)/t},p={grad:.9,turn:360,rad:360/(2*Math.PI)},b=function(e){return j(C(e))},C=function(e){return"#"===e[0]&&(e=e.substring(1)),e.length<6?{r:parseInt(e[0]+e[0],16),g:parseInt(e[1]+e[1],16),b:parseInt(e[2]+e[2],16),a:4===e.length?g(parseInt(e[3]+e[3],16)/255,2):1}:{r:parseInt(e.substring(0,2),16),g:parseInt(e.substring(2,4),16),b:parseInt(e.substring(4,6),16),a:8===e.length?g(parseInt(e.substring(6,8),16)/255,2):1}},_=function(e,r){return void 0===r&&(r="deg"),Number(e)*(p[r]||1)},E=function(e){var r=/hsla?\(?\s*(-?\d*\.?\d+)(deg|rad|grad|turn)?[,\s]+(-?\d*\.?\d+)%?[,\s]+(-?\d*\.?\d+)%?,?\s*[/\s]*(-?\d*\.?\d+)?(%)?\s*\)?/i.exec(e);return r?x({h:_(r[1],r[2]),s:Number(r[3]),l:Number(r[4]),a:void 0===r[5]?1:Number(r[5])/(r[6]?100:1)}):{h:0,s:0,v:0,a:1}},H=E,x=function(e){var r=e.s,t=e.l;return{h:e.h,s:(r*=(t<50?t:100-t)/100)>0?2*r/(t+r)*100:0,v:t+r,a:e.a}},k=function(e){return O(y(e))},M=function(e){var r=e.s,t=e.v,n=e.a,o=(200-r)*t/100;return{h:g(e.h),s:g(o>0&&o<200?r*t/100/(o<=100?o:200-o)*100:0),l:g(o/2),a:g(n,2)}},N=function(e){var r=M(e);return"hsl("+r.h+", "+r.s+"%, "+r.l+"%)"},w=function(e){var r=M(e);return"hsla("+r.h+", "+r.s+"%, "+r.l+"%, "+r.a+")"},y=function(e){var r=e.h,t=e.s,n=e.v,o=e.a;r=r/360*6,t/=100,n/=100;var a=Math.floor(r),l=n*(1-t),u=n*(1-(r-a)*t),c=n*(1-(1-r+a)*t),s=a%6;return{r:g(255*[n,u,l,l,c,n][s]),g:g(255*[c,n,n,u,l,l][s]),b:g(255*[l,l,c,n,n,u][s]),a:g(o,2)}},q=function(e){var r=/hsva?\(?\s*(-?\d*\.?\d+)(deg|rad|grad|turn)?[,\s]+(-?\d*\.?\d+)%?[,\s]+(-?\d*\.?\d+)%?,?\s*[/\s]*(-?\d*\.?\d+)?(%)?\s*\)?/i.exec(e);return r?z({h:_(r[1],r[2]),s:Number(r[3]),v:Number(r[4]),a:void 0===r[5]?1:Number(r[5])/(r[6]?100:1)}):{h:0,s:0,v:0,a:1}},P=q,R=function(e){var r=/rgba?\(?\s*(-?\d*\.?\d+)(%)?[,\s]+(-?\d*\.?\d+)(%)?[,\s]+(-?\d*\.?\d+)(%)?,?\s*[/\s]*(-?\d*\.?\d+)?(%)?\s*\)?/i.exec(e);return r?j({r:Number(r[1])/(r[2]?100/255:1),g:Number(r[3])/(r[4]?100/255:1),b:Number(r[5])/(r[6]?100/255:1),a:void 0===r[7]?1:Number(r[7])/(r[8]?100:1)}):{h:0,s:0,v:0,a:1}},I=R,S=function(e){var r=e.toString(16);return r.length<2?"0"+r:r},O=function(e){var r=e.r,t=e.g,n=e.b,o=e.a,a=o<1?S(g(255*o)):"";return"#"+S(r)+S(t)+S(n)+a},j=function(e){var r=e.r,t=e.g,n=e.b,o=e.a,a=Math.max(r,t,n),l=a-Math.min(r,t,n),u=l?a===r?(t-n)/l:a===t?2+(n-r)/l:4+(r-t)/l:0;return{h:g(60*(u<0?u+6:u)),s:g(a?l/a*100:0),v:g(a/255*100),a:o}},z=function(e){return{h:g(e.h),s:g(e.s),v:g(e.v),a:g(e.a,2)}},B=o().memo((function(e){var r=e.hue,t=e.onChange,n=h(["react-colorful__hue",e.className]);return o().createElement("div",{className:n},o().createElement(d,{onMove:function(e){t({h:360*e.left})},onKey:function(e){t({h:c(r+360*e.left,0,360)})},"aria-label":"Hue","aria-valuenow":g(r),"aria-valuemax":"360","aria-valuemin":"0"},o().createElement(m,{className:"react-colorful__hue-pointer",left:r/360,color:N({h:r,s:100,v:100,a:1})})))})),D=o().memo((function(e){var r=e.hsva,t=e.onChange,n={backgroundColor:N({h:r.h,s:100,v:100,a:1})};return o().createElement("div",{className:"react-colorful__saturation",style:n},o().createElement(d,{onMove:function(e){t({s:100*e.left,v:100-100*e.top})},onKey:function(e){t({s:c(r.s+100*e.left,0,100),v:c(r.v-100*e.top,0,100)})},"aria-label":"Color","aria-valuetext":"Saturation "+g(r.s)+"%, Brightness "+g(r.v)+"%"},o().createElement(m,{className:"react-colorful__saturation-pointer",top:1-r.v/100,left:r.s/100,color:N(r)})))})),K=function(e,r){if(e===r)return!0;for(var t in e)if(e[t]!==r[t])return!1;return!0},L=function(e,r){return e.replace(/\s/g,"")===r.replace(/\s/g,"")},A=function(e,r){return e.toLowerCase()===r.toLowerCase()||K(C(e),C(r))};function T(e,r,t){var o=u(t),a=(0,n.useState)((function(){return e.toHsva(r)})),l=a[0],c=a[1],s=(0,n.useRef)({color:r,hsva:l});(0,n.useEffect)((function(){if(!e.equal(r,s.current.color)){var t=e.toHsva(r);s.current={hsva:t,color:r},c(t)}}),[r,e]),(0,n.useEffect)((function(){var r;K(l,s.current.hsva)||e.equal(r=e.fromHsva(l),s.current.color)||(s.current={hsva:l,color:r},o(r))}),[l,e,o]);var i=(0,n.useCallback)((function(e){c((function(r){return Object.assign({},r,e)}))}),[]);return[l,i]}var F,X="undefined"!=typeof window?n.useLayoutEffect:n.useEffect,Y=function(e){F=e},V=new Map,$=function(e){X((function(){var r=e.current?e.current.ownerDocument:document;if(void 0!==r&&!V.has(r)){var n=r.createElement("style");n.innerHTML='.react-colorful{position:relative;display:flex;flex-direction:column;width:200px;height:200px;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;cursor:default}.react-colorful__saturation{position:relative;flex-grow:1;border-color:transparent;border-bottom:12px solid #000;border-radius:8px 8px 0 0;background-image:linear-gradient(0deg,#000,transparent),linear-gradient(90deg,#fff,hsla(0,0%,100%,0))}.react-colorful__alpha-gradient,.react-colorful__pointer-fill{content:"";position:absolute;left:0;top:0;right:0;bottom:0;pointer-events:none;border-radius:inherit}.react-colorful__alpha-gradient,.react-colorful__saturation{box-shadow:inset 0 0 0 1px rgba(0,0,0,.05)}.react-colorful__alpha,.react-colorful__hue{position:relative;height:24px}.react-colorful__hue{background:linear-gradient(90deg,red 0,#ff0 17%,#0f0 33%,#0ff 50%,#00f 67%,#f0f 83%,red)}.react-colorful__last-control{border-radius:0 0 8px 8px}.react-colorful__interactive{position:absolute;left:0;top:0;right:0;bottom:0;border-radius:inherit;outline:none;touch-action:none}.react-colorful__pointer{position:absolute;z-index:1;box-sizing:border-box;width:28px;height:28px;transform:translate(-50%,-50%);background-color:#fff;border:2px solid #fff;border-radius:50%;box-shadow:0 2px 4px rgba(0,0,0,.2)}.react-colorful__interactive:focus .react-colorful__pointer{transform:translate(-50%,-50%) scale(1.1)}.react-colorful__alpha,.react-colorful__alpha-pointer{background-color:#fff;background-image:url(\'data:image/svg+xml;charset=utf-8,<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill-opacity=".05"><path d="M8 0h8v8H8zM0 8h8v8H0z"/></svg>\')}.react-colorful__saturation-pointer{z-index:3}.react-colorful__hue-pointer{z-index:2}',V.set(r,n);var o=F||t.nc;o&&n.setAttribute("nonce",o),r.head.appendChild(n)}}),[])},G=function(e){var r=e.className,t=e.colorModel,u=e.color,c=void 0===u?t.defaultColor:u,s=e.onChange,i=l(e,["className","colorModel","color","onChange"]),f=(0,n.useRef)(null);$(f);var v=T(t,c,s),d=v[0],m=v[1],g=h(["react-colorful",r]);return o().createElement("div",a({},i,{ref:f,className:g}),o().createElement(D,{hsva:d,onChange:m}),o().createElement(B,{hue:d.h,onChange:m,className:"react-colorful__last-control"}))},J={defaultColor:"000",toHsva:b,fromHsva:function(e){return k({h:e.h,s:e.s,v:e.v,a:1})},equal:A},Q=function(e){return o().createElement(G,a({},e,{colorModel:J}))},U=function(e){var r=e.className,t=e.hsva,n=e.onChange,a={backgroundImage:"linear-gradient(90deg, "+w(Object.assign({},t,{a:0}))+", "+w(Object.assign({},t,{a:1}))+")"},l=h(["react-colorful__alpha",r]),u=g(100*t.a);return o().createElement("div",{className:l},o().createElement("div",{className:"react-colorful__alpha-gradient",style:a}),o().createElement(d,{onMove:function(e){n({a:e.left})},onKey:function(e){n({a:c(t.a+e.left)})},"aria-label":"Alpha","aria-valuetext":u+"%","aria-valuenow":u,"aria-valuemin":"0","aria-valuemax":"100"},o().createElement(m,{className:"react-colorful__alpha-pointer",left:t.a,color:w(t)})))},W=function(e){var r=e.className,t=e.colorModel,u=e.color,c=void 0===u?t.defaultColor:u,s=e.onChange,i=l(e,["className","colorModel","color","onChange"]),f=(0,n.useRef)(null);$(f);var v=T(t,c,s),d=v[0],m=v[1],g=h(["react-colorful",r]);return o().createElement("div",a({},i,{ref:f,className:g}),o().createElement(D,{hsva:d,onChange:m}),o().createElement(B,{hue:d.h,onChange:m}),o().createElement(U,{hsva:d,onChange:m,className:"react-colorful__last-control"}))},Z={defaultColor:"0001",toHsva:b,fromHsva:k,equal:A},ee=function(e){return o().createElement(W,a({},e,{colorModel:Z}))},re={defaultColor:{h:0,s:0,l:0,a:1},toHsva:x,fromHsva:M,equal:K},te=function(e){return o().createElement(W,a({},e,{colorModel:re}))},ne={defaultColor:"hsla(0, 0%, 0%, 1)",toHsva:E,fromHsva:w,equal:L},oe=function(e){return o().createElement(W,a({},e,{colorModel:ne}))},ae={defaultColor:{h:0,s:0,l:0},toHsva:function(e){return x({h:e.h,s:e.s,l:e.l,a:1})},fromHsva:function(e){return{h:(r=M(e)).h,s:r.s,l:r.l};var r},equal:K},le=function(e){return o().createElement(G,a({},e,{colorModel:ae}))},ue={defaultColor:"hsl(0, 0%, 0%)",toHsva:H,fromHsva:N,equal:L},ce=function(e){return o().createElement(G,a({},e,{colorModel:ue}))},se={defaultColor:{h:0,s:0,v:0,a:1},toHsva:function(e){return e},fromHsva:z,equal:K},ie=function(e){return o().createElement(W,a({},e,{colorModel:se}))},fe={defaultColor:"hsva(0, 0%, 0%, 1)",toHsva:q,fromHsva:function(e){var r=z(e);return"hsva("+r.h+", "+r.s+"%, "+r.v+"%, "+r.a+")"},equal:L},ve=function(e){return o().createElement(W,a({},e,{colorModel:fe}))},de={defaultColor:{h:0,s:0,v:0},toHsva:function(e){return{h:e.h,s:e.s,v:e.v,a:1}},fromHsva:function(e){var r=z(e);return{h:r.h,s:r.s,v:r.v}},equal:K},he=function(e){return o().createElement(G,a({},e,{colorModel:de}))},me={defaultColor:"hsv(0, 0%, 0%)",toHsva:P,fromHsva:function(e){var r=z(e);return"hsv("+r.h+", "+r.s+"%, "+r.v+"%)"},equal:L},ge=function(e){return o().createElement(G,a({},e,{colorModel:me}))},pe={defaultColor:{r:0,g:0,b:0,a:1},toHsva:j,fromHsva:y,equal:K},be=function(e){return o().createElement(W,a({},e,{colorModel:pe}))},Ce={defaultColor:"rgba(0, 0, 0, 1)",toHsva:R,fromHsva:function(e){var r=y(e);return"rgba("+r.r+", "+r.g+", "+r.b+", "+r.a+")"},equal:L},_e=function(e){return o().createElement(W,a({},e,{colorModel:Ce}))},Ee={defaultColor:{r:0,g:0,b:0},toHsva:function(e){return j({r:e.r,g:e.g,b:e.b,a:1})},fromHsva:function(e){return{r:(r=y(e)).r,g:r.g,b:r.b};var r},equal:K},He=function(e){return o().createElement(G,a({},e,{colorModel:Ee}))},xe={defaultColor:"rgb(0, 0, 0)",toHsva:I,fromHsva:function(e){var r=y(e);return"rgb("+r.r+", "+r.g+", "+r.b+")"},equal:L},ke=function(e){return o().createElement(G,a({},e,{colorModel:xe}))},Me=/^#?([0-9A-F]{3,8})$/i,Ne=function(e){var r=e.color,t=void 0===r?"":r,c=e.onChange,s=e.onBlur,i=e.escape,f=e.validate,v=e.format,d=e.process,h=l(e,["color","onChange","onBlur","escape","validate","format","process"]),m=(0,n.useState)((function(){return i(t)})),g=m[0],p=m[1],b=u(c),C=u(s),_=(0,n.useCallback)((function(e){var r=i(e.target.value);p(r),f(r)&&b(d?d(r):r)}),[i,d,f,b]),E=(0,n.useCallback)((function(e){f(e.target.value)||p(i(t)),C(e)}),[t,i,f,C]);return(0,n.useEffect)((function(){p(i(t))}),[t,i]),o().createElement("input",a({},h,{value:v?v(g):g,spellCheck:"false",onChange:_,onBlur:E}))},we=function(e){return"#"+e},ye=function(e){var r=e.prefixed,t=e.alpha,u=l(e,["prefixed","alpha"]),c=(0,n.useCallback)((function(e){return e.replace(/([^0-9A-F]+)/gi,"").substring(0,t?8:6)}),[t]),s=(0,n.useCallback)((function(e){return function(e,r){var t=Me.exec(e),n=t?t[1].length:0;return 3===n||6===n||!!r&&4===n||!!r&&8===n}(e,t)}),[t]);return o().createElement(Ne,a({},u,{escape:c,format:r?we:void 0,process:we,validate:s}))}}}]);