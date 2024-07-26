(self.webpackChunk_streamlit_app=self.webpackChunk_streamlit_app||[]).push([[2187],{70461:(e,t,r)=>{"use strict";r.d(t,{Z:()=>D});var n=r(66845),i=r(60225),a=r(17964),o=r(80745);function s(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function c(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?s(Object(r),!0).forEach((function(t){u(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):s(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function u(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}var l=(0,o.zo)("div",{position:"relative",width:"100%"});l.displayName="Root",l.displayName="Root",l.displayName="StyledRoot";var d=(0,o.zo)("div",(function(e){var t=e.$theme,r=e.$value,n=void 0===r?[]:r,i=e.$disabled,a=e.$isDragged,o=t.sizing,s="inherit";return i?s="not-allowed":a?s="grabbing":1===n.length&&(s="pointer"),{paddingTop:o.scale600,paddingBottom:o.scale600,paddingRight:o.scale600,paddingLeft:o.scale600,display:"flex",cursor:s,backgroundColor:t.colors.sliderTrackFill}}));d.displayName="Track",d.displayName="Track",d.displayName="StyledTrack";var p=(0,o.zo)("div",(function(e){var t=e.$theme,r=e.$value,n=void 0===r?[]:r,a=e.$min,o=e.$max,s=e.$disabled,c=t.colors,u=t.borders,l=t.direction,d=t.borders.useRoundedCorners?u.radius100:0;return{borderTopLeftRadius:d,borderTopRightRadius:d,borderBottomRightRadius:d,borderBottomLeftRadius:d,background:(0,i.getTrackBackground)({values:n,colors:1===n.length?[s?c.borderOpaque:c.primary,s?c.backgroundSecondary:c.borderOpaque]:[s?c.backgroundSecondary:c.borderOpaque,s?c.borderOpaque:c.primary,s?c.backgroundSecondary:c.borderOpaque],min:a||0,max:o||0,rtl:"rtl"===l}),height:"2px",width:"100%",alignSelf:"center",cursor:s?"not-allowed":"inherit"}}));p.displayName="InnerTrack",p.displayName="InnerTrack",p.displayName="StyledInnerTrack";var h=(0,o.zo)("div",(function(e){return{width:"4px",height:"2px",backgroundColor:e.$theme.colors.backgroundPrimary,marginLeft:"16px"}}));h.displayName="Mark",h.displayName="Mark",h.displayName="StyledMark";var f=(0,o.zo)("div",(function(e){return c(c({},e.$theme.typography.font200),{},{color:e.$theme.colors.contentPrimary})}));f.displayName="Tick",f.displayName="Tick",f.displayName="StyledTick";var g=(0,o.zo)("div",(function(e){var t=e.$theme.sizing;return{display:"flex",justifyContent:"space-between",alignItems:"center",paddingRight:t.scale600,paddingLeft:t.scale600,paddingBottom:t.scale400}}));g.displayName="TickBar",g.displayName="TickBar",g.displayName="StyledTickBar";var m=(0,o.zo)("div",(function(e){var t=e.$theme,r=e.$value,n=void 0===r?[]:r,i=e.$thumbIndex,a=e.$disabled,o=2===n.length&&0===i,s=2===n.length&&1===i;return"rtl"===t.direction&&(s||o)&&(o=!o,s=!s),{height:"24px",width:"24px",borderTopLeftRadius:"24px",borderTopRightRadius:"24px",borderBottomLeftRadius:"24px",borderBottomRightRadius:"24px",display:"flex",justifyContent:"center",alignItems:"center",backgroundColor:a?t.colors.sliderHandleFillDisabled:t.colors.sliderHandleFill,outline:"none",boxShadow:e.$isFocusVisible?"0 0 0 3px ".concat(t.colors.accent):"0 1px 4px rgba(0, 0, 0, 0.12)",cursor:a?"not-allowed":"inherit"}}));m.displayName="Thumb",m.displayName="Thumb",m.displayName="StyledThumb";var v=(0,o.zo)("div",(function(e){var t=e.$disabled,r=e.$theme;return{position:"absolute",top:"-16px",width:"4px",height:"20px",backgroundColor:t?r.colors.sliderHandleFillDisabled:r.colors.sliderHandleInnerFill}}));v.displayName="InnerThumb",v.displayName="InnerThumb",v.displayName="StyledInnerThumb";var b=(0,o.zo)("div",(function(e){var t=e.$disabled,r=e.$theme;return c(c({position:"absolute",top:"-".concat(r.sizing.scale1400)},r.typography.font200),{},{backgroundColor:t?r.colors.sliderHandleFillDisabled:r.colors.sliderHandleInnerFill,color:r.colors.contentInversePrimary,paddingLeft:r.sizing.scale600,paddingRight:r.sizing.scale600,paddingTop:r.sizing.scale500,paddingBottom:r.sizing.scale500,borderBottomLeftRadius:"48px",borderBottomRightRadius:"48px",borderTopLeftRadius:"48px",borderTopRightRadius:"48px",whiteSpace:"nowrap"})}));b.displayName="ThumbValue",b.displayName="ThumbValue",b.displayName="StyledThumbValue";var y=r(80318),k=r(42274);function w(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function x(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?w(Object(r),!0).forEach((function(t){T(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):w(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function T(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function O(){return O=Object.assign?Object.assign.bind():function(e){for(var t=1;t<arguments.length;t++){var r=arguments[t];for(var n in r)Object.prototype.hasOwnProperty.call(r,n)&&(e[n]=r[n])}return e},O.apply(this,arguments)}function M(e,t){return function(e){if(Array.isArray(e))return e}(e)||function(e,t){var r=null==e?null:"undefined"!==typeof Symbol&&e[Symbol.iterator]||e["@@iterator"];if(null==r)return;var n,i,a=[],o=!0,s=!1;try{for(r=r.call(e);!(o=(n=r.next()).done)&&(a.push(n.value),!t||a.length!==t);o=!0);}catch(c){s=!0,i=c}finally{try{o||null==r.return||r.return()}finally{if(s)throw i}}return a}(e,t)||function(e,t){if(!e)return;if("string"===typeof e)return R(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);"Object"===r&&e.constructor&&(r=e.constructor.name);if("Map"===r||"Set"===r)return Array.from(e);if("Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r))return R(e,t)}(e,t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()}function R(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,n=new Array(t);r<t;r++)n[r]=e[r];return n}const D=function(e){var t=e.overrides,r=void 0===t?{}:t,o=e.disabled,s=void 0!==o&&o,c=e.marks,u=void 0!==c&&c,w=e.onChange,T=void 0===w?function(){}:w,R=e.onFinalChange,D=void 0===R?function(){}:R,S=e.min,E=void 0===S?0:S,I=e.max,j=void 0===I?100:I,_=e.step,C=void 0===_?1:_,P=e.persistentThumb,L=void 0!==P&&P,z=e.valueToLabel,F=void 0===z?function(e){return e}:z,$=e.value,A=n.useContext(k.N),B=M(n.useState(!1),2),N=B[0],V=B[1],U=M(n.useState(!1),2),X=U[0],Y=U[1],Z=M(n.useState(!1),2),q=Z[0],H=Z[1],K=M(n.useState(-1),2),W=K[0],J=K[1],G=n.useCallback((function(e){(0,a.E)(e)&&H(!0);var t=e.target.parentNode.firstChild===e.target?0:1;J(t)}),[]),Q=n.useCallback((function(e){!1!==q&&H(!1),J(-1)}),[]),ee=function(e){if(e.length>2||0===e.length)throw new Error("the value prop represents positions of thumbs, so its length can be only one or two");return e}($),te={$disabled:s,$step:C,$min:E,$max:j,$marks:u,$value:ee,$isFocusVisible:q},re=M((0,y.jb)(r.Root,l),2),ne=re[0],ie=re[1],ae=M((0,y.jb)(r.Track,d),2),oe=ae[0],se=ae[1],ce=M((0,y.jb)(r.InnerTrack,p),2),ue=ce[0],le=ce[1],de=M((0,y.jb)(r.Thumb,m),2),pe=de[0],he=de[1],fe=M((0,y.jb)(r.InnerThumb,v),2),ge=fe[0],me=fe[1],ve=M((0,y.jb)(r.ThumbValue,b),2),be=ve[0],ye=ve[1],ke=M((0,y.jb)(r.Tick,f),2),we=ke[0],xe=ke[1],Te=M((0,y.jb)(r.TickBar,g),2),Oe=Te[0],Me=Te[1],Re=M((0,y.jb)(r.Mark,h),2),De=Re[0],Se=Re[1];return n.createElement(ne,O({"data-baseweb":"slider"},te,ie,{onFocus:(0,a.Ah)(ie,G),onBlur:(0,a.Z5)(ie,Q)}),n.createElement(i.Range,O({step:C,min:E,max:j,values:ee,disabled:s,onChange:function(e){return T({value:e})},onFinalChange:function(e){return D({value:e})},rtl:"rtl"===A.direction,renderTrack:function(e){var t=e.props,r=e.children,i=e.isDragged;return n.createElement(oe,O({onMouseDown:t.onMouseDown,onTouchStart:t.onTouchStart,$isDragged:i},te,se),n.createElement(ue,O({$isDragged:i,ref:t.ref},te,le),r))},renderThumb:function(e){var t=e.props,r=e.index,i=e.isDragged,a=L||(!!r&&X||!r&&N||i)&&!s;return n.createElement(pe,O({},t,{onMouseEnter:function(){0===r?V(!0):Y(!0)},onMouseLeave:function(){0===r?V(!1):Y(!1)},$thumbIndex:r,$isDragged:i,style:x({},t.style)},te,he,{$isFocusVisible:q&&W===r}),a&&n.createElement(be,O({$thumbIndex:r,$isDragged:i},te,ye),F(ee[r])),a&&n.createElement(ge,O({$thumbIndex:r,$isDragged:i},te,me)))}},u?{renderMark:function(e){var t=e.props,r=e.index;return n.createElement(De,O({$markIndex:r},t,te,Se))}}:{})),n.createElement(Oe,O({},te,Me),n.createElement(we,O({},te,xe),F(E)),n.createElement(we,O({},te,xe),F(j))))}},42786:function(e,t,r){"use strict";var n=this&&this.__extends||function(){var e=function(t,r){return e=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(e,t){e.__proto__=t}||function(e,t){for(var r in t)Object.prototype.hasOwnProperty.call(t,r)&&(e[r]=t[r])},e(t,r)};return function(t,r){if("function"!==typeof r&&null!==r)throw new TypeError("Class extends value "+String(r)+" is not a constructor or null");function n(){this.constructor=t}e(t,r),t.prototype=null===r?Object.create(r):(n.prototype=r.prototype,new n)}}(),i=this&&this.__createBinding||(Object.create?function(e,t,r,n){void 0===n&&(n=r);var i=Object.getOwnPropertyDescriptor(t,r);i&&!("get"in i?!t.__esModule:i.writable||i.configurable)||(i={enumerable:!0,get:function(){return t[r]}}),Object.defineProperty(e,n,i)}:function(e,t,r,n){void 0===n&&(n=r),e[n]=t[r]}),a=this&&this.__setModuleDefault||(Object.create?function(e,t){Object.defineProperty(e,"default",{enumerable:!0,value:t})}:function(e,t){e.default=t}),o=this&&this.__importStar||function(e){if(e&&e.__esModule)return e;var t={};if(null!=e)for(var r in e)"default"!==r&&Object.prototype.hasOwnProperty.call(e,r)&&i(t,e,r);return a(t,e),t},s=this&&this.__spreadArray||function(e,t,r){if(r||2===arguments.length)for(var n,i=0,a=t.length;i<a;i++)!n&&i in t||(n||(n=Array.prototype.slice.call(t,0,i)),n[i]=t[i]);return e.concat(n||Array.prototype.slice.call(t))};Object.defineProperty(t,"__esModule",{value:!0});var c=o(r(66845)),u=r(13335),l=r(94722),d=["ArrowRight","ArrowUp","k","PageUp"],p=["ArrowLeft","ArrowDown","j","PageDown"],h=function(e){function t(t){var r=e.call(this,t)||this;if(r.trackRef=c.createRef(),r.thumbRefs=[],r.state={draggedTrackPos:[-1,-1],draggedThumbIndex:-1,thumbZIndexes:new Array(r.props.values.length).fill(0).map((function(e,t){return t})),isChanged:!1,markOffsets:[]},r.getOffsets=function(){var e=r.props,t=e.direction,n=e.values,i=e.min,a=e.max,o=r.trackRef.current,s=o.getBoundingClientRect(),c=(0,u.getPaddingAndBorder)(o);return r.getThumbs().map((function(e,r){var o={x:0,y:0},d=e.getBoundingClientRect(),p=(0,u.getMargin)(e);switch(t){case l.Direction.Right:return o.x=-1*(p.left+c.left),o.y=-1*((d.height-s.height)/2+c.top),o.x+=s.width*(0,u.relativeValue)(n[r],i,a)-d.width/2,o;case l.Direction.Left:return o.x=-1*(p.right+c.right),o.y=-1*((d.height-s.height)/2+c.top),o.x+=s.width-s.width*(0,u.relativeValue)(n[r],i,a)-d.width/2,o;case l.Direction.Up:return o.x=-1*((d.width-s.width)/2+p.left+c.left),o.y=-c.left,o.y+=s.height-s.height*(0,u.relativeValue)(n[r],i,a)-d.height/2,o;case l.Direction.Down:return o.x=-1*((d.width-s.width)/2+p.left+c.left),o.y=-c.left,o.y+=s.height*(0,u.relativeValue)(n[r],i,a)-d.height/2,o;default:return(0,u.assertUnreachable)(t)}}))},r.getThumbs=function(){return r.trackRef&&r.trackRef.current?Array.from(r.trackRef.current.children).filter((function(e){return e.hasAttribute("aria-valuenow")})):(console.warn("No thumbs found in the track container. Did you forget to pass & spread the `props` param in renderTrack?"),[])},r.getTargetIndex=function(e){return r.getThumbs().findIndex((function(t){return t===e.target||t.contains(e.target)}))},r.addTouchEvents=function(e){document.addEventListener("touchmove",r.schdOnTouchMove,{passive:!1}),document.addEventListener("touchend",r.schdOnEnd,{passive:!1}),document.addEventListener("touchcancel",r.schdOnEnd,{passive:!1})},r.addMouseEvents=function(e){document.addEventListener("mousemove",r.schdOnMouseMove),document.addEventListener("mouseup",r.schdOnEnd)},r.onMouseDownTrack=function(e){var t;if(0===e.button)if(e.persist(),e.preventDefault(),r.addMouseEvents(e.nativeEvent),r.props.values.length>1&&r.props.draggableTrack){if(r.thumbRefs.some((function(t){var r;return null===(r=t.current)||void 0===r?void 0:r.contains(e.target)})))return;r.setState({draggedTrackPos:[e.clientX,e.clientY]},(function(){return r.onMove(e.clientX,e.clientY)}))}else{var n=(0,u.getClosestThumbIndex)(r.thumbRefs.map((function(e){return e.current})),e.clientX,e.clientY,r.props.direction);null===(t=r.thumbRefs[n].current)||void 0===t||t.focus(),r.setState({draggedThumbIndex:n},(function(){return r.onMove(e.clientX,e.clientY)}))}},r.onResize=function(){(0,u.translateThumbs)(r.getThumbs(),r.getOffsets(),r.props.rtl),r.calculateMarkOffsets()},r.onTouchStartTrack=function(e){var t;if(e.persist(),r.addTouchEvents(e.nativeEvent),r.props.values.length>1&&r.props.draggableTrack){if(r.thumbRefs.some((function(t){var r;return null===(r=t.current)||void 0===r?void 0:r.contains(e.target)})))return;r.setState({draggedTrackPos:[e.touches[0].clientX,e.touches[0].clientY]},(function(){return r.onMove(e.touches[0].clientX,e.touches[0].clientY)}))}else{var n=(0,u.getClosestThumbIndex)(r.thumbRefs.map((function(e){return e.current})),e.touches[0].clientX,e.touches[0].clientY,r.props.direction);null===(t=r.thumbRefs[n].current)||void 0===t||t.focus(),r.setState({draggedThumbIndex:n},(function(){return r.onMove(e.touches[0].clientX,e.touches[0].clientY)}))}},r.onMouseOrTouchStart=function(e){if(!r.props.disabled){var t=(0,u.isTouchEvent)(e);if(t||0===e.button){var n=r.getTargetIndex(e);-1!==n&&(t?r.addTouchEvents(e):r.addMouseEvents(e),r.setState({draggedThumbIndex:n,thumbZIndexes:r.state.thumbZIndexes.map((function(e,t){return t===n?Math.max.apply(Math,r.state.thumbZIndexes):e<=r.state.thumbZIndexes[n]?e:e-1}))}))}}},r.onMouseMove=function(e){e.preventDefault(),r.onMove(e.clientX,e.clientY)},r.onTouchMove=function(e){e.preventDefault(),r.onMove(e.touches[0].clientX,e.touches[0].clientY)},r.onKeyDown=function(e){var t=r.props,n=t.values,i=t.onChange,a=t.step,o=t.rtl,s=t.direction,c=r.state.isChanged,h=r.getTargetIndex(e.nativeEvent),f=o||s===l.Direction.Left||s===l.Direction.Down?-1:1;-1!==h&&(d.includes(e.key)?(e.preventDefault(),r.setState({draggedThumbIndex:h,isChanged:!0}),i((0,u.replaceAt)(n,h,r.normalizeValue(n[h]+f*("PageUp"===e.key?10*a:a),h)))):p.includes(e.key)?(e.preventDefault(),r.setState({draggedThumbIndex:h,isChanged:!0}),i((0,u.replaceAt)(n,h,r.normalizeValue(n[h]-f*("PageDown"===e.key?10*a:a),h)))):"Tab"===e.key?r.setState({draggedThumbIndex:-1},(function(){c&&r.fireOnFinalChange()})):c&&r.fireOnFinalChange())},r.onKeyUp=function(e){var t=r.state.isChanged;r.setState({draggedThumbIndex:-1},(function(){t&&r.fireOnFinalChange()}))},r.onMove=function(e,t){var n=r.state,i=n.draggedThumbIndex,a=n.draggedTrackPos,o=r.props,s=o.direction,c=o.min,d=o.max,p=o.onChange,h=o.values,f=o.step,g=o.rtl;if(-1===i&&-1===a[0]&&-1===a[1])return null;var m=r.trackRef.current;if(!m)return null;var v=m.getBoundingClientRect(),b=(0,u.isVertical)(s)?v.height:v.width;if(-1!==a[0]&&-1!==a[1]){var y=e-a[0],k=t-a[1],w=0;switch(s){case l.Direction.Right:case l.Direction.Left:w=y/b*(d-c);break;case l.Direction.Down:case l.Direction.Up:w=k/b*(d-c);break;default:(0,u.assertUnreachable)(s)}if(g&&(w*=-1),Math.abs(w)>=f/2){for(var x=0;x<r.thumbRefs.length;x++){if(h[x]===d&&1===Math.sign(w)||h[x]===c&&-1===Math.sign(w))return;var T=h[x]+w;T>d?w=d-h[x]:T<c&&(w=c-h[x])}var O=h.slice(0);for(x=0;x<r.thumbRefs.length;x++)O=(0,u.replaceAt)(O,x,r.normalizeValue(h[x]+w,x));r.setState({draggedTrackPos:[e,t]}),p(O)}}else{var M=0;switch(s){case l.Direction.Right:M=(e-v.left)/b*(d-c)+c;break;case l.Direction.Left:M=(b-(e-v.left))/b*(d-c)+c;break;case l.Direction.Down:M=(t-v.top)/b*(d-c)+c;break;case l.Direction.Up:M=(b-(t-v.top))/b*(d-c)+c;break;default:(0,u.assertUnreachable)(s)}g&&(M=d+c-M),Math.abs(h[i]-M)>=f/2&&p((0,u.replaceAt)(h,i,r.normalizeValue(M,i)))}},r.normalizeValue=function(e,t){var n=r.props,i=n.min,a=n.max,o=n.step,s=n.allowOverlap,c=n.values;return(0,u.normalizeValue)(e,t,i,a,o,s,c)},r.onEnd=function(e){if(e.preventDefault(),document.removeEventListener("mousemove",r.schdOnMouseMove),document.removeEventListener("touchmove",r.schdOnTouchMove),document.removeEventListener("mouseup",r.schdOnEnd),document.removeEventListener("touchend",r.schdOnEnd),document.removeEventListener("touchcancel",r.schdOnEnd),-1===r.state.draggedThumbIndex&&-1===r.state.draggedTrackPos[0]&&-1===r.state.draggedTrackPos[1])return null;r.setState({draggedThumbIndex:-1,draggedTrackPos:[-1,-1]},(function(){r.fireOnFinalChange()}))},r.fireOnFinalChange=function(){r.setState({isChanged:!1});var e=r.props,t=e.onFinalChange,n=e.values;t&&t(n)},r.updateMarkRefs=function(e){if(!e.renderMark)return r.numOfMarks=void 0,void(r.markRefs=void 0);r.numOfMarks=(e.max-e.min)/r.props.step,r.markRefs=[];for(var t=0;t<r.numOfMarks+1;t++)r.markRefs[t]=c.createRef()},r.calculateMarkOffsets=function(){if(r.props.renderMark&&r.trackRef&&r.numOfMarks&&r.markRefs&&null!==r.trackRef.current){for(var e=window.getComputedStyle(r.trackRef.current),t=parseInt(e.width,10),n=parseInt(e.height,10),i=parseInt(e.paddingLeft,10),a=parseInt(e.paddingTop,10),o=[],s=0;s<r.numOfMarks+1;s++){var c=9999,u=9999;if(r.markRefs[s].current){var d=r.markRefs[s].current.getBoundingClientRect();c=d.height,u=d.width}r.props.direction===l.Direction.Left||r.props.direction===l.Direction.Right?o.push([Math.round(t/r.numOfMarks*s+i-u/2),-Math.round((c-n)/2)]):o.push([Math.round(n/r.numOfMarks*s+a-c/2),-Math.round((u-t)/2)])}r.setState({markOffsets:o})}},0===t.step)throw new Error('"step" property should be a positive number');return r.schdOnMouseMove=(0,u.schd)(r.onMouseMove),r.schdOnTouchMove=(0,u.schd)(r.onTouchMove),r.schdOnEnd=(0,u.schd)(r.onEnd),r.thumbRefs=t.values.map((function(){return c.createRef()})),r.updateMarkRefs(t),r}return n(t,e),t.prototype.componentDidMount=function(){var e=this,t=this.props,r=t.values,n=t.min,i=t.step;this.resizeObserver=window.ResizeObserver?new window.ResizeObserver(this.onResize):{observe:function(){return window.addEventListener("resize",e.onResize)},unobserve:function(){return window.removeEventListener("resize",e.onResize)}},document.addEventListener("touchstart",this.onMouseOrTouchStart,{passive:!1}),document.addEventListener("mousedown",this.onMouseOrTouchStart,{passive:!1}),!this.props.allowOverlap&&(0,u.checkInitialOverlap)(this.props.values),this.props.values.forEach((function(t){return(0,u.checkBoundaries)(t,e.props.min,e.props.max)})),this.resizeObserver.observe(this.trackRef.current),(0,u.translateThumbs)(this.getThumbs(),this.getOffsets(),this.props.rtl),this.calculateMarkOffsets(),r.forEach((function(e){(0,u.isStepDivisible)(n,e,i)||console.warn("The `values` property is in conflict with the current `step`, `min`, and `max` properties. Please provide values that are accessible using the min, max, and step values.")}))},t.prototype.componentDidUpdate=function(e,t){var r=this.props,n=r.max,i=r.min,a=r.step,o=r.values,s=r.rtl;e.max===n&&e.min===i&&e.step===a||this.updateMarkRefs(this.props),(0,u.translateThumbs)(this.getThumbs(),this.getOffsets(),s),e.max===n&&e.min===i&&e.step===a&&t.markOffsets.length===this.state.markOffsets.length||(this.calculateMarkOffsets(),o.forEach((function(e){(0,u.isStepDivisible)(i,e,a)||console.warn("The `values` property is in conflict with the current `step`, `min`, and `max` properties. Please provide values that are accessible using the min, max, and step values.")})))},t.prototype.componentWillUnmount=function(){document.removeEventListener("mousedown",this.onMouseOrTouchStart,{passive:!1}),document.removeEventListener("mousemove",this.schdOnMouseMove),document.removeEventListener("touchmove",this.schdOnTouchMove),document.removeEventListener("touchstart",this.onMouseOrTouchStart),document.removeEventListener("mouseup",this.schdOnEnd),document.removeEventListener("touchend",this.schdOnEnd),this.resizeObserver.unobserve(this.trackRef.current)},t.prototype.render=function(){var e=this,t=this.props,r=t.renderTrack,n=t.renderThumb,i=t.renderMark,a=void 0===i?function(){return null}:i,o=t.values,c=t.min,d=t.max,p=t.allowOverlap,h=t.disabled,f=this.state,g=f.draggedThumbIndex,m=f.thumbZIndexes,v=f.markOffsets;return r({props:{style:{transform:"scale(1)",cursor:g>-1?"grabbing":this.props.draggableTrack?(0,u.isVertical)(this.props.direction)?"ns-resize":"ew-resize":1!==o.length||h?"inherit":"pointer"},onMouseDown:h?u.voidFn:this.onMouseDownTrack,onTouchStart:h?u.voidFn:this.onTouchStartTrack,ref:this.trackRef},isDragged:this.state.draggedThumbIndex>-1,disabled:h,children:s(s([],v.map((function(t,r,n){return a({props:{style:e.props.direction===l.Direction.Left||e.props.direction===l.Direction.Right?{position:"absolute",left:"".concat(t[0],"px"),marginTop:"".concat(t[1],"px")}:{position:"absolute",top:"".concat(t[0],"px"),marginLeft:"".concat(t[1],"px")},key:"mark".concat(r),ref:e.markRefs[r]},index:r})})),!0),o.map((function(t,r){var i=e.state.draggedThumbIndex===r;return n({index:r,value:t,isDragged:i,props:{style:{position:"absolute",zIndex:m[r],cursor:h?"inherit":i?"grabbing":"grab",userSelect:"none",touchAction:"none",WebkitUserSelect:"none",MozUserSelect:"none",msUserSelect:"none"},key:r,tabIndex:h?void 0:0,"aria-valuemax":p?d:o[r+1]||d,"aria-valuemin":p?c:o[r-1]||c,"aria-valuenow":t,draggable:!1,ref:e.thumbRefs[r],role:"slider",onKeyDown:h?u.voidFn:e.onKeyDown,onKeyUp:h?u.voidFn:e.onKeyUp}})})),!0)})},t.defaultProps={step:1,direction:l.Direction.Right,rtl:!1,disabled:!1,allowOverlap:!1,draggableTrack:!1,min:0,max:100},t}(c.Component);t.default=h},60225:function(e,t,r){"use strict";var n=this&&this.__importDefault||function(e){return e&&e.__esModule?e:{default:e}};Object.defineProperty(t,"__esModule",{value:!0}),t.checkValuesAgainstBoundaries=t.relativeValue=t.useThumbOverlap=t.Direction=t.getTrackBackground=t.Range=void 0;var i=n(r(42786));t.Range=i.default;var a=r(13335);Object.defineProperty(t,"getTrackBackground",{enumerable:!0,get:function(){return a.getTrackBackground}}),Object.defineProperty(t,"useThumbOverlap",{enumerable:!0,get:function(){return a.useThumbOverlap}}),Object.defineProperty(t,"relativeValue",{enumerable:!0,get:function(){return a.relativeValue}}),Object.defineProperty(t,"checkValuesAgainstBoundaries",{enumerable:!0,get:function(){return a.checkValuesAgainstBoundaries}});var o=r(94722);Object.defineProperty(t,"Direction",{enumerable:!0,get:function(){return o.Direction}})},94722:(e,t)=>{"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.Direction=void 0,function(e){e.Right="to right",e.Left="to left",e.Down="to bottom",e.Up="to top"}(t.Direction||(t.Direction={}))},13335:function(e,t,r){"use strict";var n=this&&this.__spreadArray||function(e,t,r){if(r||2===arguments.length)for(var n,i=0,a=t.length;i<a;i++)!n&&i in t||(n||(n=Array.prototype.slice.call(t,0,i)),n[i]=t[i]);return e.concat(n||Array.prototype.slice.call(t))};Object.defineProperty(t,"__esModule",{value:!0}),t.useThumbOverlap=t.assertUnreachable=t.voidFn=t.getTrackBackground=t.replaceAt=t.schd=t.translate=t.getClosestThumbIndex=t.translateThumbs=t.getPaddingAndBorder=t.getMargin=t.checkInitialOverlap=t.checkValuesAgainstBoundaries=t.checkBoundaries=t.isVertical=t.relativeValue=t.normalizeValue=t.isStepDivisible=t.isTouchEvent=t.getStepDecimals=void 0;var i=r(66845),a=r(94722);function o(e){return e===a.Direction.Up||e===a.Direction.Down}function s(e,t,r){e.style.transform="translate(".concat(t,"px, ").concat(r,"px)")}t.getStepDecimals=function(e){var t=e.toString().split(".")[1];return t?t.length:0},t.isTouchEvent=function(e){return e.touches&&e.touches.length||e.changedTouches&&e.changedTouches.length},t.isStepDivisible=function(e,t,r){var n=Number(((t-e)/r).toFixed(8));return parseInt(n.toString(),10)===n},t.normalizeValue=function(e,r,n,i,a,o,s){var c=1e11;if(e=Math.round(e*c)/c,!o){var u=s[r-1],l=s[r+1];if(u&&u>e)return u;if(l&&l<e)return l}if(e>i)return i;if(e<n)return n;var d=Math.floor(e*c-n*c)%Math.floor(a*c),p=Math.floor(e*c-Math.abs(d)),h=0===d?e:p/c,f=Math.abs(d/c)<a/2?h:h+a,g=(0,t.getStepDecimals)(a);return parseFloat(f.toFixed(g))},t.relativeValue=function(e,t,r){return(e-t)/(r-t)},t.isVertical=o,t.checkBoundaries=function(e,t,r){if(t>=r)throw new RangeError("min (".concat(t,") is equal/bigger than max (").concat(r,")"));if(e<t)throw new RangeError("value (".concat(e,") is smaller than min (").concat(t,")"));if(e>r)throw new RangeError("value (".concat(e,") is bigger than max (").concat(r,")"))},t.checkValuesAgainstBoundaries=function(e,t,r){return e<t?t:e>r?r:e},t.checkInitialOverlap=function(e){if(!(e.length<2)&&!e.slice(1).every((function(t,r){return e[r]<=t})))throw new RangeError("values={[".concat(e,"]} needs to be sorted when allowOverlap={false}"))},t.getMargin=function(e){var t=window.getComputedStyle(e);return{top:parseInt(t["margin-top"],10),bottom:parseInt(t["margin-bottom"],10),left:parseInt(t["margin-left"],10),right:parseInt(t["margin-right"],10)}},t.getPaddingAndBorder=function(e){var t=window.getComputedStyle(e);return{top:parseInt(t["padding-top"],10)+parseInt(t["border-top-width"],10),bottom:parseInt(t["padding-bottom"],10)+parseInt(t["border-bottom-width"],10),left:parseInt(t["padding-left"],10)+parseInt(t["border-left-width"],10),right:parseInt(t["padding-right"],10)+parseInt(t["border-right-width"],10)}},t.translateThumbs=function(e,t,r){var n=r?-1:1;e.forEach((function(e,r){return s(e,n*t[r].x,t[r].y)}))},t.getClosestThumbIndex=function(e,t,r,n){for(var i=0,a=u(e[0],t,r,n),o=1;o<e.length;o++){var s=u(e[o],t,r,n);s<a&&(a=s,i=o)}return i},t.translate=s;t.schd=function(e){var t=[],r=null;return function(){for(var n=[],i=0;i<arguments.length;i++)n[i]=arguments[i];t=n,r||(r=requestAnimationFrame((function(){r=null,e.apply(void 0,t)})))}},t.replaceAt=function(e,t,r){var n=e.slice(0);return n[t]=r,n},t.getTrackBackground=function(e){var t=e.values,r=e.colors,n=e.min,i=e.max,o=e.direction,s=void 0===o?a.Direction.Right:o,c=e.rtl,u=void 0!==c&&c;u&&s===a.Direction.Right?s=a.Direction.Left:u&&a.Direction.Left&&(s=a.Direction.Right);var l=t.slice(0).sort((function(e,t){return e-t})).map((function(e){return(e-n)/(i-n)*100})).reduce((function(e,t,n){return"".concat(e,", ").concat(r[n]," ").concat(t,"%, ").concat(r[n+1]," ").concat(t,"%")}),"");return"linear-gradient(".concat(s,", ").concat(r[0]," 0%").concat(l,", ").concat(r[r.length-1]," 100%)")},t.voidFn=function(){},t.assertUnreachable=function(e){throw new Error("Didn't expect to get here")};var c=function(e,t,r,i,a){return void 0===a&&(a=function(e){return e}),Math.ceil(n([e],Array.from(e.children),!0).reduce((function(e,n){var o=Math.ceil(n.getBoundingClientRect().width);if(n.innerText&&n.innerText.includes(r)&&0===n.childElementCount){var s=n.cloneNode(!0);s.innerHTML=a(t.toFixed(i)),s.style.visibility="hidden",document.body.appendChild(s),o=Math.ceil(s.getBoundingClientRect().width),document.body.removeChild(s)}return o>e?o:e}),e.getBoundingClientRect().width))};function u(e,t,r,n){var i=e.getBoundingClientRect(),a=i.left,s=i.top,c=i.width,u=i.height;return o(n)?Math.abs(r-(s+u/2)):Math.abs(t-(a+c/2))}t.useThumbOverlap=function(e,r,a,o,s,u){void 0===o&&(o=.1),void 0===s&&(s=" - "),void 0===u&&(u=function(e){return e});var l=(0,t.getStepDecimals)(o),d=(0,i.useState)({}),p=d[0],h=d[1],f=(0,i.useState)(u(r[a].toFixed(l))),g=f[0],m=f[1];return(0,i.useEffect)((function(){if(e){var t=e.getThumbs();if(t.length<1)return;var i={},o=e.getOffsets(),d=function(e,t,r,i,a,o,s){void 0===s&&(s=function(e){return e});var u=[],l=function(e){var d=c(r[e],i[e],a,o,s),p=t[e].x;t.forEach((function(t,h){var f=t.x,g=c(r[h],i[h],a,o,s);e!==h&&(p>=f&&p<=f+g||p+d>=f&&p+d<=f+g)&&(u.includes(h)||(u.push(e),u.push(h),u=n(n([],u,!0),[e,h],!1),l(h)))}))};return l(e),Array.from(new Set(u.sort()))}(a,o,t,r,s,l,u),p=u(r[a].toFixed(l));if(d.length){var f=d.reduce((function(e,t,r,i){return e.length?n(n([],e,!0),[o[i[r]].x],!1):[o[i[r]].x]}),[]);if(Math.min.apply(Math,f)===o[a].x){var g=[];d.forEach((function(e){g.push(r[e].toFixed(l))})),p=Array.from(new Set(g.sort((function(e,t){return parseFloat(e)-parseFloat(t)})))).map(u).join(s);var v=Math.min.apply(Math,f),b=Math.max.apply(Math,f),y=t[d[f.indexOf(b)]].getBoundingClientRect().width;i.left="".concat(Math.abs(v-(b+y))/2,"px"),i.transform="translate(-50%, 0)"}else i.visibility="hidden"}m(p),h(i)}}),[e,r]),[g,p]}},52347:(e,t,r)=>{var n;!function(){"use strict";var i={not_string:/[^s]/,not_bool:/[^t]/,not_type:/[^T]/,not_primitive:/[^v]/,number:/[diefg]/,numeric_arg:/[bcdiefguxX]/,json:/[j]/,not_json:/[^j]/,text:/^[^\x25]+/,modulo:/^\x25{2}/,placeholder:/^\x25(?:([1-9]\d*)\$|\(([^)]+)\))?(\+)?(0|'[^$])?(-)?(\d+)?(?:\.(\d+))?([b-gijostTuvxX])/,key:/^([a-z_][a-z_\d]*)/i,key_access:/^\.([a-z_][a-z_\d]*)/i,index_access:/^\[(\d+)\]/,sign:/^[+-]/};function a(e){return function(e,t){var r,n,o,s,c,u,l,d,p,h=1,f=e.length,g="";for(n=0;n<f;n++)if("string"===typeof e[n])g+=e[n];else if("object"===typeof e[n]){if((s=e[n]).keys)for(r=t[h],o=0;o<s.keys.length;o++){if(void 0==r)throw new Error(a('[sprintf] Cannot access property "%s" of undefined value "%s"',s.keys[o],s.keys[o-1]));r=r[s.keys[o]]}else r=s.param_no?t[s.param_no]:t[h++];if(i.not_type.test(s.type)&&i.not_primitive.test(s.type)&&r instanceof Function&&(r=r()),i.numeric_arg.test(s.type)&&"number"!==typeof r&&isNaN(r))throw new TypeError(a("[sprintf] expecting number but found %T",r));switch(i.number.test(s.type)&&(d=r>=0),s.type){case"b":r=parseInt(r,10).toString(2);break;case"c":r=String.fromCharCode(parseInt(r,10));break;case"d":case"i":r=parseInt(r,10);break;case"j":r=JSON.stringify(r,null,s.width?parseInt(s.width):0);break;case"e":r=s.precision?parseFloat(r).toExponential(s.precision):parseFloat(r).toExponential();break;case"f":r=s.precision?parseFloat(r).toFixed(s.precision):parseFloat(r);break;case"g":r=s.precision?String(Number(r.toPrecision(s.precision))):parseFloat(r);break;case"o":r=(parseInt(r,10)>>>0).toString(8);break;case"s":r=String(r),r=s.precision?r.substring(0,s.precision):r;break;case"t":r=String(!!r),r=s.precision?r.substring(0,s.precision):r;break;case"T":r=Object.prototype.toString.call(r).slice(8,-1).toLowerCase(),r=s.precision?r.substring(0,s.precision):r;break;case"u":r=parseInt(r,10)>>>0;break;case"v":r=r.valueOf(),r=s.precision?r.substring(0,s.precision):r;break;case"x":r=(parseInt(r,10)>>>0).toString(16);break;case"X":r=(parseInt(r,10)>>>0).toString(16).toUpperCase()}i.json.test(s.type)?g+=r:(!i.number.test(s.type)||d&&!s.sign?p="":(p=d?"+":"-",r=r.toString().replace(i.sign,"")),u=s.pad_char?"0"===s.pad_char?"0":s.pad_char.charAt(1):" ",l=s.width-(p+r).length,c=s.width&&l>0?u.repeat(l):"",g+=s.align?p+r+c:"0"===u?p+c+r:c+p+r)}return g}(function(e){if(s[e])return s[e];var t,r=e,n=[],a=0;for(;r;){if(null!==(t=i.text.exec(r)))n.push(t[0]);else if(null!==(t=i.modulo.exec(r)))n.push("%");else{if(null===(t=i.placeholder.exec(r)))throw new SyntaxError("[sprintf] unexpected placeholder");if(t[2]){a|=1;var o=[],c=t[2],u=[];if(null===(u=i.key.exec(c)))throw new SyntaxError("[sprintf] failed to parse named argument key");for(o.push(u[1]);""!==(c=c.substring(u[0].length));)if(null!==(u=i.key_access.exec(c)))o.push(u[1]);else{if(null===(u=i.index_access.exec(c)))throw new SyntaxError("[sprintf] failed to parse named argument key");o.push(u[1])}t[2]=o}else a|=2;if(3===a)throw new Error("[sprintf] mixing positional and named placeholders is not (yet) supported");n.push({placeholder:t[0],param_no:t[1],keys:t[2],sign:t[3],pad_char:t[4],align:t[5],width:t[6],precision:t[7],type:t[8]})}r=r.substring(t[0].length)}return s[e]=n}(e),arguments)}function o(e,t){return a.apply(null,[e].concat(t||[]))}var s=Object.create(null);t.sprintf=a,t.vsprintf=o,"undefined"!==typeof window&&(window.sprintf=a,window.vsprintf=o,void 0===(n=function(){return{sprintf:a,vsprintf:o}}.call(t,r,t,e))||(e.exports=n))}()}}]);