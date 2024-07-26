/*! For license information please see 4040.613bd8c0.chunk.js.LICENSE.txt */
"use strict";(self.webpackChunkreact_admin_upgrade=self.webpackChunkreact_admin_upgrade||[]).push([[4040],{44040:function(e,n,t){t.r(n),t.d(n,{conf:function(){return o},language:function(){return r}});var o={comments:{lineComment:"'",blockComment:["/*","*/"]},brackets:[["{","}"],["[","]"],["(",")"],["<",">"],["addhandler","end addhandler"],["class","end class"],["enum","end enum"],["event","end event"],["function","end function"],["get","end get"],["if","end if"],["interface","end interface"],["module","end module"],["namespace","end namespace"],["operator","end operator"],["property","end property"],["raiseevent","end raiseevent"],["removehandler","end removehandler"],["select","end select"],["set","end set"],["structure","end structure"],["sub","end sub"],["synclock","end synclock"],["try","end try"],["while","end while"],["with","end with"],["using","end using"],["do","loop"],["for","next"]],autoClosingPairs:[{open:"{",close:"}",notIn:["string","comment"]},{open:"[",close:"]",notIn:["string","comment"]},{open:"(",close:")",notIn:["string","comment"]},{open:'"',close:'"',notIn:["string","comment"]},{open:"<",close:">",notIn:["string","comment"]}],folding:{markers:{start:new RegExp("^\\s*#Region\\b"),end:new RegExp("^\\s*#End Region\\b")}}},r={defaultToken:"",tokenPostfix:".vb",ignoreCase:!0,brackets:[{token:"delimiter.bracket",open:"{",close:"}"},{token:"delimiter.array",open:"[",close:"]"},{token:"delimiter.parenthesis",open:"(",close:")"},{token:"delimiter.angle",open:"<",close:">"},{token:"keyword.tag-addhandler",open:"addhandler",close:"end addhandler"},{token:"keyword.tag-class",open:"class",close:"end class"},{token:"keyword.tag-enum",open:"enum",close:"end enum"},{token:"keyword.tag-event",open:"event",close:"end event"},{token:"keyword.tag-function",open:"function",close:"end function"},{token:"keyword.tag-get",open:"get",close:"end get"},{token:"keyword.tag-if",open:"if",close:"end if"},{token:"keyword.tag-interface",open:"interface",close:"end interface"},{token:"keyword.tag-module",open:"module",close:"end module"},{token:"keyword.tag-namespace",open:"namespace",close:"end namespace"},{token:"keyword.tag-operator",open:"operator",close:"end operator"},{token:"keyword.tag-property",open:"property",close:"end property"},{token:"keyword.tag-raiseevent",open:"raiseevent",close:"end raiseevent"},{token:"keyword.tag-removehandler",open:"removehandler",close:"end removehandler"},{token:"keyword.tag-select",open:"select",close:"end select"},{token:"keyword.tag-set",open:"set",close:"end set"},{token:"keyword.tag-structure",open:"structure",close:"end structure"},{token:"keyword.tag-sub",open:"sub",close:"end sub"},{token:"keyword.tag-synclock",open:"synclock",close:"end synclock"},{token:"keyword.tag-try",open:"try",close:"end try"},{token:"keyword.tag-while",open:"while",close:"end while"},{token:"keyword.tag-with",open:"with",close:"end with"},{token:"keyword.tag-using",open:"using",close:"end using"},{token:"keyword.tag-do",open:"do",close:"loop"},{token:"keyword.tag-for",open:"for",close:"next"}],keywords:["AddHandler","AddressOf","Alias","And","AndAlso","As","Async","Boolean","ByRef","Byte","ByVal","Call","Case","Catch","CBool","CByte","CChar","CDate","CDbl","CDec","Char","CInt","Class","CLng","CObj","Const","Continue","CSByte","CShort","CSng","CStr","CType","CUInt","CULng","CUShort","Date","Decimal","Declare","Default","Delegate","Dim","DirectCast","Do","Double","Each","Else","ElseIf","End","EndIf","Enum","Erase","Error","Event","Exit","False","Finally","For","Friend","Function","Get","GetType","GetXMLNamespace","Global","GoSub","GoTo","Handles","If","Implements","Imports","In","Inherits","Integer","Interface","Is","IsNot","Let","Lib","Like","Long","Loop","Me","Mod","Module","MustInherit","MustOverride","MyBase","MyClass","NameOf","Namespace","Narrowing","New","Next","Not","Nothing","NotInheritable","NotOverridable","Object","Of","On","Operator","Option","Optional","Or","OrElse","Out","Overloads","Overridable","Overrides","ParamArray","Partial","Private","Property","Protected","Public","RaiseEvent","ReadOnly","ReDim","RemoveHandler","Resume","Return","SByte","Select","Set","Shadows","Shared","Short","Single","Static","Step","Stop","String","Structure","Sub","SyncLock","Then","Throw","To","True","Try","TryCast","TypeOf","UInteger","ULong","UShort","Using","Variant","Wend","When","While","Widening","With","WithEvents","WriteOnly","Xor"],tagwords:["If","Sub","Select","Try","Class","Enum","Function","Get","Interface","Module","Namespace","Operator","Set","Structure","Using","While","With","Do","Loop","For","Next","Property","Continue","AddHandler","RemoveHandler","Event","RaiseEvent","SyncLock"],symbols:/[=><!~?;\.,:&|+\-*\/\^%]+/,integersuffix:/U?[DI%L&S@]?/,floatsuffix:/[R#F!]?/,tokenizer:{root:[{include:"@whitespace"},[/next(?!\w)/,{token:"keyword.tag-for"}],[/loop(?!\w)/,{token:"keyword.tag-do"}],[/end\s+(?!for|do)(addhandler|class|enum|event|function|get|if|interface|module|namespace|operator|property|raiseevent|removehandler|select|set|structure|sub|synclock|try|while|with|using)/,{token:"keyword.tag-$1"}],[/[a-zA-Z_]\w*/,{cases:{"@tagwords":{token:"keyword.tag-$0"},"@keywords":{token:"keyword.$0"},"@default":"identifier"}}],[/^\s*#\w+/,"keyword"],[/\d*\d+e([\-+]?\d+)?(@floatsuffix)/,"number.float"],[/\d*\.\d+(e[\-+]?\d+)?(@floatsuffix)/,"number.float"],[/&H[0-9a-f]+(@integersuffix)/,"number.hex"],[/&0[0-7]+(@integersuffix)/,"number.octal"],[/\d+(@integersuffix)/,"number"],[/#.*#/,"number"],[/[{}()\[\]]/,"@brackets"],[/@symbols/,"delimiter"],[/["\u201c\u201d]/,{token:"string.quote",next:"@string"}]],whitespace:[[/[ \t\r\n]+/,""],[/(\'|REM(?!\w)).*$/,"comment"]],string:[[/[^"\u201c\u201d]+/,"string"],[/["\u201c\u201d]{2}/,"string.escape"],[/["\u201c\u201d]C?/,{token:"string.quote",next:"@pop"}]]}}}}]);
//# sourceMappingURL=4040.613bd8c0.chunk.js.map