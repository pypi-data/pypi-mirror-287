"use strict";(self.webpackChunk_streamlit_app=self.webpackChunk_streamlit_app||[]).push([[4177],{94177:(e,t,i)=>{i.r(t),i.d(t,{default:()=>d});var s=i(66845),r=i(87814),o=i(74516),l=i(50641),a=i(40864);class n extends s.PureComponent{constructor(){super(...arguments),this.formClearHelper=new r.K,this.state={value:this.initialValue},this.commitWidgetValue=e=>{const{widgetMgr:t,element:i,fragmentId:s}=this.props;t.setStringValue(i,this.state.value,e,s)},this.onFormCleared=()=>{this.setState(((e,t)=>({value:t.element.default})),(()=>this.commitWidgetValue({fromUi:!0})))},this.onColorClose=e=>{this.setState({value:e},(()=>this.commitWidgetValue({fromUi:!0})))}}get initialValue(){const e=this.props.widgetMgr.getStringValue(this.props.element);return void 0!==e?e:this.props.element.default}componentDidMount(){this.props.element.setValue?this.updateFromProtobuf():this.commitWidgetValue({fromUi:!1})}componentDidUpdate(){this.maybeUpdateFromProtobuf()}componentWillUnmount(){this.formClearHelper.disconnect()}maybeUpdateFromProtobuf(){const{setValue:e}=this.props.element;e&&this.updateFromProtobuf()}updateFromProtobuf(){const{value:e}=this.props.element;this.props.element.setValue=!1,this.setState({value:e},(()=>{this.commitWidgetValue({fromUi:!1})}))}render(){var e;const{element:t,width:i,disabled:s,widgetMgr:r}=this.props,{value:n}=this.state;return this.formClearHelper.manageFormClearListener(r,t.formId,this.onFormCleared),(0,a.jsx)(o.Z,{label:t.label,labelVisibility:(0,l.iF)(null===(e=t.labelVisibility)||void 0===e?void 0:e.value),help:t.help,onChange:this.onColorClose,disabled:s,width:i,value:n})}}const d=n},87814:(e,t,i)=>{i.d(t,{K:()=>r});var s=i(50641);class r{constructor(){this.formClearListener=void 0,this.lastWidgetMgr=void 0,this.lastFormId=void 0}manageFormClearListener(e,t,i){null!=this.formClearListener&&this.lastWidgetMgr===e&&this.lastFormId===t||(this.disconnect(),(0,s.bM)(t)&&(this.formClearListener=e.addFormClearedListener(t,i),this.lastWidgetMgr=e,this.lastFormId=t))}disconnect(){var e;null===(e=this.formClearListener)||void 0===e||e.disconnect(),this.formClearListener=void 0,this.lastWidgetMgr=void 0,this.lastFormId=void 0}}}}]);