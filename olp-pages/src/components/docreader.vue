<template lang="html">
  <div class="doc-reader" style="margin-top: 62px;">
    <div class="doc-contents" id="markdown-doc-content">
      <!-- <p>目录</p> -->
    </div>
    <div class="markdown-body" id="markdown-container">
    </div>
    <div class="float-clear">
    </div>
  </div>
</template>

<script>
import $ from 'jquery';

export default {
  name: 'DocReader',
  data () {
    return {
      id: this.docid,
      content: `&lt;h1&gt;Markdown 语法简介&lt;/h1&gt;
&lt;blockquote&gt;
&lt;p&gt;&lt;a href="http://commonmark.org/help/" target="_blank"&gt;语法详解&lt;/a&gt;&lt;/p&gt;
&lt;/blockquote&gt;
&lt;h2&gt;&lt;strong&gt;粗体&lt;/strong&gt;&lt;/h2&gt;
&lt;h3&gt;&lt;strong&gt;粗体&lt;/strong&gt;&lt;/h3&gt;
&lt;pre&gt;&lt;code class="lang-"&gt;**粗体**
__粗体__
&lt;/code&gt;&lt;/pre&gt;
&lt;h2&gt;&lt;em&gt;斜体&lt;/em&gt;&lt;/h2&gt;
&lt;pre&gt;&lt;code class="lang-"&gt;*斜体*
_斜体_
&lt;/code&gt;&lt;/pre&gt;
&lt;h2&gt;标题&lt;/h2&gt;
&lt;pre&gt;&lt;code class="lang-"&gt;# 一级标题 #
一级标题
====
## 二级标题 ##
二级标题
----
### 三级标题 ###
#### 四级标题 ####
##### 五级标题 #####
###### 六级标题 ######
&lt;/code&gt;&lt;/pre&gt;
&lt;h2&gt;分割线&lt;/h2&gt;
&lt;pre&gt;&lt;code class="lang-"&gt;***
---
&lt;/code&gt;&lt;/pre&gt;
&lt;hr&gt;
&lt;h2&gt;&lt;sup&gt;上&lt;/sup&gt;角&lt;sub&gt;下&lt;/sub&gt;标&lt;/h2&gt;
&lt;pre&gt;&lt;code class="lang-"&gt;上角标 x^2^
下角标 H~2~0
&lt;/code&gt;&lt;/pre&gt;
&lt;h2&gt;&lt;ins&gt;下划线&lt;/ins&gt; &lt;s&gt;中划线&lt;/s&gt;&lt;/h2&gt;
&lt;pre&gt;&lt;code class="lang-"&gt;++下划线++
~~中划线~~
&lt;/code&gt;&lt;/pre&gt;
&lt;h2&gt;&lt;mark&gt;标记&lt;/mark&gt;&lt;/h2&gt;
&lt;pre&gt;&lt;code class="lang-"&gt;==标记==
&lt;/code&gt;&lt;/pre&gt;
&lt;h2&gt;段落引用&lt;/h2&gt;
&lt;pre&gt;&lt;code class="lang-"&gt;&amp;gt; 一级
&amp;gt;&amp;gt; 二级
&amp;gt;&amp;gt;&amp;gt; 三级
...
&lt;/code&gt;&lt;/pre&gt;
&lt;h2&gt;列表&lt;/h2&gt;
&lt;pre&gt;&lt;code class="lang-"&gt;有序列表
1.
2.
3.
...
无序列表
-
-
...
&lt;/code&gt;&lt;/pre&gt;
&lt;h2&gt;任务列表&lt;/h2&gt;
&lt;ul class="contains-task-list"&gt;
&lt;li class="task-list-item"&gt;&lt;input class="task-list-item-checkbox" checked="" disabled="" type="checkbox"&gt; 已完成任务&lt;/li&gt;
&lt;li class="task-list-item"&gt;&lt;input class="task-list-item-checkbox" disabled="" type="checkbox"&gt; 未完成任务&lt;/li&gt;
&lt;/ul&gt;
&lt;pre&gt;&lt;code class="lang-"&gt;- [x] 已完成任务
- [ ] 未完成任务
&lt;/code&gt;&lt;/pre&gt;
&lt;h2&gt;链接&lt;/h2&gt;
&lt;pre&gt;&lt;code class="lang-"&gt;[链接](www.baidu.com)
![图片描述](http://www.image.com)
&lt;/code&gt;&lt;/pre&gt;
&lt;h2&gt;代码段落&lt;/h2&gt;
&lt;p&gt;\`\`\` type&lt;/p&gt;
&lt;p&gt;代码段落&lt;/p&gt;
&lt;p&gt;\`\`\`&lt;/p&gt;
&lt;p&gt;\` 代码块 \`&lt;/p&gt;
&lt;pre&gt;&lt;div class="hljs"&gt;&lt;code class="lang-c++"&gt;&lt;span class="hljs-function"&gt;&lt;span class="hljs-keyword"&gt;int&lt;/span&gt; &lt;span class="hljs-title"&gt;main&lt;/span&gt;&lt;span class="hljs-params"&gt;()&lt;/span&gt;
&lt;/span&gt;{
    &lt;span class="hljs-built_in"&gt;printf&lt;/span&gt;(&lt;span class="hljs-string"&gt;"hello world!"&lt;/span&gt;);
}
&lt;/code&gt;&lt;/div&gt;&lt;/pre&gt;
&lt;p&gt;&lt;code&gt;code&lt;/code&gt;&lt;/p&gt;
&lt;h2&gt;表格(table)&lt;/h2&gt;
&lt;pre&gt;&lt;code class="lang-"&gt;| 标题1 | 标题2 | 标题3 |
| :--  | :--: | ----: |
| 左对齐 | 居中 | 右对齐 |
| ---------------------- | ------------- | ----------------- |
&lt;/code&gt;&lt;/pre&gt;
&lt;table&gt;
&lt;thead&gt;
&lt;tr&gt;
&lt;th style="text-align:left"&gt;标题1&lt;/th&gt;
&lt;th style="text-align:center"&gt;标题2&lt;/th&gt;
&lt;th style="text-align:right"&gt;标题3&lt;/th&gt;
&lt;/tr&gt;
&lt;/thead&gt;
&lt;tbody&gt;
&lt;tr&gt;
&lt;td style="text-align:left"&gt;左对齐&lt;/td&gt;
&lt;td style="text-align:center"&gt;居中&lt;/td&gt;
&lt;td style="text-align:right"&gt;右对齐&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td style="text-align:left"&gt;----------------------&lt;/td&gt;
&lt;td style="text-align:center"&gt;-------------&lt;/td&gt;
&lt;td style="text-align:right"&gt;-----------------&lt;/td&gt;
&lt;/tr&gt;
&lt;/tbody&gt;
&lt;/table&gt;
&lt;h2&gt;脚注(footnote)&lt;/h2&gt;
&lt;pre&gt;&lt;code class="lang-"&gt;hello[^hello]
&lt;/code&gt;&lt;/pre&gt;
&lt;p&gt;见底部脚注&lt;sup class="footnote-ref"&gt;&lt;a href="#fn1" id="fnref1"&gt;[1]&lt;/a&gt;&lt;/sup&gt;&lt;/p&gt;
&lt;h2&gt;表情(emoji)&lt;/h2&gt;
&lt;p&gt;&lt;a href="https://www.webpagefx.com/tools/emoji-cheat-sheet/" target="_blank"&gt;参考网站: https://www.webpagefx.com/tools/emoji-cheat-sheet/&lt;/a&gt;&lt;/p&gt;
&lt;pre&gt;&lt;code class="lang-"&gt;:laughing:
:blush:
:smiley:
:)
...
&lt;/code&gt;&lt;/pre&gt;
&lt;p&gt;😆😊😃😃&lt;/p&gt;
&lt;h2&gt;&lt;span class="katex"&gt;&lt;span class="katex-mathml"&gt;&lt;math&gt;&lt;semantics&gt;&lt;mrow&gt;&lt;mtext&gt;KaTeX&lt;/mtext&gt;&lt;/mrow&gt;&lt;annotation encoding="application/x-tex"&gt;\KaTeX&lt;/annotation&gt;&lt;/semantics&gt;&lt;/math&gt;&lt;/span&gt;&lt;span class="katex-html" aria-hidden="true"&gt;&lt;span class="strut" style="height:0.68333em;"&gt;&lt;/span&gt;&lt;span class="strut bottom" style="height:1.0302031249999999em;vertical-align:-0.34687312499999995em;"&gt;&lt;/span&gt;&lt;span class="base"&gt;&lt;span class="mord katex-logo"&gt;&lt;span class="k"&gt;K&lt;/span&gt;&lt;span class="a"&gt;A&lt;/span&gt;&lt;span class="t"&gt;T&lt;/span&gt;&lt;span class="e"&gt;E&lt;/span&gt;&lt;span class="x"&gt;X&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;公式&lt;/h2&gt;
&lt;p&gt;我们可以渲染公式例如：&lt;span class="katex"&gt;&lt;span class="katex-mathml"&gt;&lt;math&gt;&lt;semantics&gt;&lt;mrow&gt;&lt;msub&gt;&lt;mi&gt;x&lt;/mi&gt;&lt;mi&gt;i&lt;/mi&gt;&lt;/msub&gt;&lt;mo&gt;+&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;y&lt;/mi&gt;&lt;mi&gt;i&lt;/mi&gt;&lt;/msub&gt;&lt;mo&gt;=&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;z&lt;/mi&gt;&lt;mi&gt;i&lt;/mi&gt;&lt;/msub&gt;&lt;/mrow&gt;&lt;annotation encoding="application/x-tex"&gt;x_i + y_i = z_i&lt;/annotation&gt;&lt;/semantics&gt;&lt;/math&gt;&lt;/span&gt;&lt;span class="katex-html" aria-hidden="true"&gt;&lt;span class="strut" style="height:0.58333em;"&gt;&lt;/span&gt;&lt;span class="strut bottom" style="height:0.7777700000000001em;vertical-align:-0.19444em;"&gt;&lt;/span&gt;&lt;span class="base"&gt;&lt;span class="mord"&gt;&lt;span class="mord mathit"&gt;x&lt;/span&gt;&lt;span class="msupsub"&gt;&lt;span class="vlist-t vlist-t2"&gt;&lt;span class="vlist-r"&gt;&lt;span class="vlist" style="height:0.31166399999999994em;"&gt;&lt;span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"&gt;&lt;span class="pstrut" style="height:2.7em;"&gt;&lt;/span&gt;&lt;span class="sizing reset-size6 size3 mtight"&gt;&lt;span class="mord mathit mtight"&gt;i&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;span class="vlist-s"&gt;​&lt;/span&gt;&lt;/span&gt;&lt;span class="vlist-r"&gt;&lt;span class="vlist" style="height:0.15em;"&gt;&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;span class="mbin"&gt;+&lt;/span&gt;&lt;span class="mord"&gt;&lt;span class="mord mathit" style="margin-right:0.03588em;"&gt;y&lt;/span&gt;&lt;span class="msupsub"&gt;&lt;span class="vlist-t vlist-t2"&gt;&lt;span class="vlist-r"&gt;&lt;span class="vlist" style="height:0.31166399999999994em;"&gt;&lt;span style="top:-2.5500000000000003em;margin-left:-0.03588em;margin-right:0.05em;"&gt;&lt;span class="pstrut" style="height:2.7em;"&gt;&lt;/span&gt;&lt;span class="sizing reset-size6 size3 mtight"&gt;&lt;span class="mord mathit mtight"&gt;i&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;span class="vlist-s"&gt;​&lt;/span&gt;&lt;/span&gt;&lt;span class="vlist-r"&gt;&lt;span class="vlist" style="height:0.15em;"&gt;&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;span class="mrel"&gt;=&lt;/span&gt;&lt;span class="mord"&gt;&lt;span class="mord mathit" style="margin-right:0.04398em;"&gt;z&lt;/span&gt;&lt;span class="msupsub"&gt;&lt;span class="vlist-t vlist-t2"&gt;&lt;span class="vlist-r"&gt;&lt;span class="vlist" style="height:0.31166399999999994em;"&gt;&lt;span style="top:-2.5500000000000003em;margin-left:-0.04398em;margin-right:0.05em;"&gt;&lt;span class="pstrut" style="height:2.7em;"&gt;&lt;/span&gt;&lt;span class="sizing reset-size6 size3 mtight"&gt;&lt;span class="mord mathit mtight"&gt;i&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;span class="vlist-s"&gt;​&lt;/span&gt;&lt;/span&gt;&lt;span class="vlist-r"&gt;&lt;span class="vlist" style="height:0.15em;"&gt;&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;和&lt;span class="katex"&gt;&lt;span class="katex-mathml"&gt;&lt;math&gt;&lt;semantics&gt;&lt;mrow&gt;&lt;msubsup&gt;&lt;mo&gt;∑&lt;/mo&gt;&lt;mrow&gt;&lt;mi&gt;i&lt;/mi&gt;&lt;mo&gt;=&lt;/mo&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;/mrow&gt;&lt;mi&gt;n&lt;/mi&gt;&lt;/msubsup&gt;&lt;msub&gt;&lt;mi&gt;a&lt;/mi&gt;&lt;mi&gt;i&lt;/mi&gt;&lt;/msub&gt;&lt;mo&gt;=&lt;/mo&gt;&lt;mn&gt;0&lt;/mn&gt;&lt;/mrow&gt;&lt;annotation encoding="application/x-tex"&gt;\sum_{i=1}^n a_i=0&lt;/annotation&gt;&lt;/semantics&gt;&lt;/math&gt;&lt;/span&gt;&lt;span class="katex-html" aria-hidden="true"&gt;&lt;span class="strut" style="height:0.804292em;"&gt;&lt;/span&gt;&lt;span class="strut bottom" style="height:1.104002em;vertical-align:-0.29971000000000003em;"&gt;&lt;/span&gt;&lt;span class="base"&gt;&lt;span class="mop"&gt;&lt;span class="mop op-symbol small-op" style="position:relative;top:-0.0000050000000000050004em;"&gt;∑&lt;/span&gt;&lt;span class="msupsub"&gt;&lt;span class="vlist-t vlist-t2"&gt;&lt;span class="vlist-r"&gt;&lt;span class="vlist" style="height:0.804292em;"&gt;&lt;span style="top:-2.40029em;margin-left:0em;margin-right:0.05em;"&gt;&lt;span class="pstrut" style="height:2.7em;"&gt;&lt;/span&gt;&lt;span class="sizing reset-size6 size3 mtight"&gt;&lt;span class="mord mtight"&gt;&lt;span class="mord mathit mtight"&gt;i&lt;/span&gt;&lt;span class="mrel mtight"&gt;=&lt;/span&gt;&lt;span class="mord mathrm mtight"&gt;1&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;span style="top:-3.2029em;margin-right:0.05em;"&gt;&lt;span class="pstrut" style="height:2.7em;"&gt;&lt;/span&gt;&lt;span class="sizing reset-size6 size3 mtight"&gt;&lt;span class="mord mathit mtight"&gt;n&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;span class="vlist-s"&gt;​&lt;/span&gt;&lt;/span&gt;&lt;span class="vlist-r"&gt;&lt;span class="vlist" style="height:0.29971000000000003em;"&gt;&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;span class="mord"&gt;&lt;span class="mord mathit"&gt;a&lt;/span&gt;&lt;span class="msupsub"&gt;&lt;span class="vlist-t vlist-t2"&gt;&lt;span class="vlist-r"&gt;&lt;span class="vlist" style="height:0.31166399999999994em;"&gt;&lt;span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"&gt;&lt;span class="pstrut" style="height:2.7em;"&gt;&lt;/span&gt;&lt;span class="sizing reset-size6 size3 mtight"&gt;&lt;span class="mord mathit mtight"&gt;i&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;span class="vlist-s"&gt;​&lt;/span&gt;&lt;/span&gt;&lt;span class="vlist-r"&gt;&lt;span class="vlist" style="height:0.15em;"&gt;&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;span class="mrel"&gt;=&lt;/span&gt;&lt;span class="mord mathrm"&gt;0&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;br&gt;
我们也可以单行渲染&lt;/p&gt;
&lt;p&gt;&lt;span class="katex-display"&gt;&lt;span class="katex"&gt;&lt;span class="katex-mathml"&gt;&lt;math&gt;&lt;semantics&gt;&lt;mrow&gt;&lt;munderover&gt;&lt;mo&gt;∑&lt;/mo&gt;&lt;mrow&gt;&lt;mi&gt;i&lt;/mi&gt;&lt;mo&gt;=&lt;/mo&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;/mrow&gt;&lt;mi&gt;n&lt;/mi&gt;&lt;/munderover&gt;&lt;msub&gt;&lt;mi&gt;a&lt;/mi&gt;&lt;mi&gt;i&lt;/mi&gt;&lt;/msub&gt;&lt;mo&gt;=&lt;/mo&gt;&lt;mn&gt;0&lt;/mn&gt;&lt;/mrow&gt;&lt;annotation encoding="application/x-tex"&gt;\sum_{i=1}^n a_i=0
&lt;/annotation&gt;&lt;/semantics&gt;&lt;/math&gt;&lt;/span&gt;&lt;span class="katex-html" aria-hidden="true"&gt;&lt;span class="strut" style="height:1.6513970000000002em;"&gt;&lt;/span&gt;&lt;span class="strut bottom" style="height:2.929066em;vertical-align:-1.277669em;"&gt;&lt;/span&gt;&lt;span class="base"&gt;&lt;span class="mop op-limits"&gt;&lt;span class="vlist-t vlist-t2"&gt;&lt;span class="vlist-r"&gt;&lt;span class="vlist" style="height:1.6513970000000002em;"&gt;&lt;span style="top:-1.872331em;margin-left:0em;"&gt;&lt;span class="pstrut" style="height:3.05em;"&gt;&lt;/span&gt;&lt;span class="sizing reset-size6 size3 mtight"&gt;&lt;span class="mord mtight"&gt;&lt;span class="mord mathit mtight"&gt;i&lt;/span&gt;&lt;span class="mrel mtight"&gt;=&lt;/span&gt;&lt;span class="mord mathrm mtight"&gt;1&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;span style="top:-3.050005em;"&gt;&lt;span class="pstrut" style="height:3.05em;"&gt;&lt;/span&gt;&lt;span&gt;&lt;span class="mop op-symbol large-op"&gt;∑&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;span style="top:-4.3000050000000005em;margin-left:0em;"&gt;&lt;span class="pstrut" style="height:3.05em;"&gt;&lt;/span&gt;&lt;span class="sizing reset-size6 size3 mtight"&gt;&lt;span class="mord mathit mtight"&gt;n&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;span class="vlist-s"&gt;​&lt;/span&gt;&lt;/span&gt;&lt;span class="vlist-r"&gt;&lt;span class="vlist" style="height:1.277669em;"&gt;&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;span class="mord"&gt;&lt;span class="mord mathit"&gt;a&lt;/span&gt;&lt;span class="msupsub"&gt;&lt;span class="vlist-t vlist-t2"&gt;&lt;span class="vlist-r"&gt;&lt;span class="vlist" style="height:0.31166399999999994em;"&gt;&lt;span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"&gt;&lt;span class="pstrut" style="height:2.7em;"&gt;&lt;/span&gt;&lt;span class="sizing reset-size6 size3 mtight"&gt;&lt;span class="mord mathit mtight"&gt;i&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;span class="vlist-s"&gt;​&lt;/span&gt;&lt;/span&gt;&lt;span class="vlist-r"&gt;&lt;span class="vlist" style="height:0.15em;"&gt;&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;span class="mrel"&gt;=&lt;/span&gt;&lt;span class="mord mathrm"&gt;0&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;/p&gt;
&lt;p&gt;具体可参照&lt;a href="http://www.intmath.com/cg5/katex-mathjax-comparison.php" target="_blank"&gt;katex文档&lt;/a&gt;和&lt;a href="https://github.com/Khan/KaTeX/wiki/Function-Support-in-KaTeX" target="_blank"&gt;katex支持的函数&lt;/a&gt;以及&lt;a href="https://math.meta.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference" target="_blank"&gt;latex文档&lt;/a&gt;&lt;/p&gt;
&lt;h2&gt;布局&lt;/h2&gt;
&lt;div class="hljs-left"&gt;
&lt;p&gt;&lt;code&gt;::: hljs-left&lt;/code&gt;&lt;br&gt;
&lt;code&gt;居左&lt;/code&gt;&lt;br&gt;
&lt;code&gt;:::&lt;/code&gt;&lt;/p&gt;
&lt;/div&gt;
&lt;div class="hljs-center"&gt;
&lt;p&gt;&lt;code&gt;::: hljs-center&lt;/code&gt;&lt;br&gt;
&lt;code&gt;居中&lt;/code&gt;&lt;br&gt;
&lt;code&gt;:::&lt;/code&gt;&lt;/p&gt;
&lt;/div&gt;
&lt;div class="hljs-right"&gt;
&lt;p&gt;&lt;code&gt;::: hljs-right&lt;/code&gt;&lt;br&gt;
&lt;code&gt;居右&lt;/code&gt;&lt;br&gt;
&lt;code&gt;:::&lt;/code&gt;&lt;/p&gt;
&lt;/div&gt;
&lt;h2&gt;定义&lt;/h2&gt;
&lt;dl&gt;
&lt;dt&gt;术语一&lt;/dt&gt;
&lt;dd&gt;
&lt;p&gt;定义一&lt;/p&gt;
&lt;/dd&gt;
&lt;dt&gt;包含有&lt;em&gt;行内标记&lt;/em&gt;的术语二&lt;/dt&gt;
&lt;dd&gt;
&lt;p&gt;定义二&lt;/p&gt;
&lt;pre&gt;&lt;code&gt;  {一些定义二的文字或代码}
&lt;/code&gt;&lt;/pre&gt;
&lt;p&gt;定义二的第三段&lt;/p&gt;
&lt;/dd&gt;
&lt;/dl&gt;
&lt;pre&gt;&lt;code class="lang-"&gt;术语一

:   定义一

包含有*行内标记*的术语二

:   定义二

        {一些定义二的文字或代码}

    定义二的第三段

&lt;/code&gt;&lt;/pre&gt;
&lt;h2&gt;abbr&lt;/h2&gt;
&lt;p&gt;&lt;abbr title="Hyper Text Markup Language"&gt;HTML&lt;/abbr&gt; 规范由 &lt;abbr title="World Wide Web Consortium"&gt;W3C&lt;/abbr&gt; 维护&lt;/p&gt;
&lt;pre&gt;&lt;code class="lang-"&gt;*[HTML]: Hyper Text Markup Language
*[W3C]:  World Wide Web Consortium
HTML 规范由 W3C 维护
&lt;/code&gt;&lt;/pre&gt;
&lt;hr class="footnotes-sep"&gt;
&lt;section class="footnotes"&gt;
&lt;ol class="footnotes-list"&gt;
&lt;li id="fn1" class="footnote-item"&gt;&lt;p&gt;一个注脚 &lt;a href="#fnref1" class="footnote-backref"&gt;↩︎&lt;/a&gt;&lt;/p&gt;
&lt;/li&gt;
&lt;/ol&gt;
&lt;/section&gt;
`
    }
  },
  props: ['docid'],
  methods: {},
  mounted () {
    $('#markdown-container').html($('#markdown-container').html(this.content).text());
    $('#markdown-container').find('h2,h3').each(function(index, item) {
      var thisId = "header-"+index;
      $(this).attr('id', thisId);
      var tagName = $(this)[0].tagName.toLowerCase();
      var headerText = $(this).text();
      var root = window.location.href;
      var ele = "<a href='#"+thisId+"'><"+tagName+">"+headerText+"</"+tagName+"></a>";
      $("#markdown-doc-content").append($(ele));
    })
  }
}
</script>

<style lang="css">
/* pre {
    display: block;
    padding: 9.5px;
    margin: 0 0 10px;
    font-size: 13px;
    line-height: 1.42857143;
    word-break: break-all;
    word-wrap: break-word;
    color: #333;
    background-color: #f5f5f5;
    border: 1px solid #ccc;
    border-radius: 4px;
    overflow-x: auto;
} */
sup, sub {
  z-index: inherit;
}

.doc-contents {
  width: 300px;
  height: 550px;
  background-color: #fff;
  float: left;
  padding: 25px 25px 60px;
  text-align: left;
  position: fixed;
  overflow-y: auto;
}
.markdown-body {
  width: 865px;
  float: right;
  background-color: #fff;
  padding: 25px 35px 15px;
  text-align: left;
}

a>h2 {
  padding-bottom: 10px;
}
a>h3 {
  padding-left: 10px;
  padding-bottom: 10px;
}

@font-face {
  font-family: octicons-link;
}

.markdown-body {
  line-height: 1.5;
  color: #24292e;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
  font-size: 16px;
  line-height: 1.5;
  word-wrap: break-word;
}

.markdown-body .pl-c {
  color: #6a737d;
}

.markdown-body .pl-c1,
.markdown-body .pl-s .pl-v {
  color: #005cc5;
}

.markdown-body .pl-e,
.markdown-body .pl-en {
  color: #6f42c1;
}

.markdown-body .pl-smi,
.markdown-body .pl-s .pl-s1 {
  color: #24292e;
}

.markdown-body .pl-ent {
  color: #22863a;
}

.markdown-body .pl-k {
  color: #d73a49;
}

.markdown-body .pl-s,
.markdown-body .pl-pds,
.markdown-body .pl-s .pl-pse .pl-s1,
.markdown-body .pl-sr,
.markdown-body .pl-sr .pl-cce,
.markdown-body .pl-sr .pl-sre,
.markdown-body .pl-sr .pl-sra {
  color: #032f62;
}

.markdown-body .pl-v,
.markdown-body .pl-smw {
  color: #e36209;
}

.markdown-body .pl-bu {
  color: #b31d28;
}

.markdown-body .pl-ii {
  color: #fafbfc;
  background-color: #b31d28;
}

.markdown-body .pl-c2 {
  color: #fafbfc;
  background-color: #d73a49;
}

.markdown-body .pl-c2::before {
  content: "^M";
}

.markdown-body .pl-sr .pl-cce {
  font-weight: bold;
  color: #22863a;
}

.markdown-body .pl-ml {
  color: #735c0f;
}

.markdown-body .pl-mh,
.markdown-body .pl-mh .pl-en,
.markdown-body .pl-ms {
  font-weight: bold;
  color: #005cc5;
}

.markdown-body .pl-mi {
  font-style: italic;
  color: #24292e;
}

.markdown-body .pl-mb {
  font-weight: bold;
  color: #24292e;
}

.markdown-body .pl-md {
  color: #b31d28;
  background-color: #ffeef0;
}

.markdown-body .pl-mi1 {
  color: #22863a;
  background-color: #f0fff4;
}

.markdown-body .pl-mc {
  color: #e36209;
  background-color: #ffebda;
}

.markdown-body .pl-mi2 {
  color: #f6f8fa;
  background-color: #005cc5;
}

.markdown-body .pl-mdr {
  font-weight: bold;
  color: #6f42c1;
}

.markdown-body .pl-ba {
  color: #586069;
}

.markdown-body .pl-sg {
  color: #959da5;
}

.markdown-body .pl-corl {
  text-decoration: underline;
  color: #032f62;
}

.markdown-body .octicon {
  display: inline-block;
  vertical-align: text-top;
  fill: currentColor;
}

.markdown-body a {
  background-color: transparent;
  -webkit-text-decoration-skip: objects;
}

.markdown-body a:active,
.markdown-body a:hover {
  outline-width: 0;
}

.markdown-body strong {
  font-weight: inherit;
}

.markdown-body strong {
  font-weight: bolder;
}

.markdown-body h1 {
  font-size: 2em;
  margin: 0.67em 0;
}

.markdown-body img {
  border-style: none;
}

.markdown-body svg:not(:root) {
  overflow: hidden;
}

.markdown-body code,
.markdown-body kbd,
.markdown-body pre {
  font-family: monospace, monospace;
  font-size: 1em;
}

.markdown-body hr {
  box-sizing: content-box;
  height: 0;
  overflow: visible;
}

.markdown-body input {
  font: inherit;
  margin: 0;
}

.markdown-body input {
  overflow: visible;
}

.markdown-body [type="checkbox"] {
  box-sizing: border-box;
  padding: 0;
}

.markdown-body * {
  box-sizing: border-box;
}

.markdown-body input {
  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
}

.markdown-body a {
  color: #0366d6;
  text-decoration: none;
}

.markdown-body a:hover {
  text-decoration: underline;
}

.markdown-body strong {
  font-weight: 600;
}

.markdown-body hr {
  height: 0;
  margin: 15px 0;
  overflow: hidden;
  background: transparent;
  border: 0;
  border-bottom: 1px solid #dfe2e5;
}

.markdown-body hr::before {
  display: table;
  content: "";
}

.markdown-body hr::after {
  display: table;
  clear: both;
  content: "";
}

.markdown-body table {
  border-spacing: 0;
  border-collapse: collapse;
}

.markdown-body td,
.markdown-body th {
  padding: 0;
}

.markdown-body h1,
.markdown-body h2,
.markdown-body h3,
.markdown-body h4,
.markdown-body h5,
.markdown-body h6 {
  margin-top: 0;
  margin-bottom: 0;
}

.markdown-body h1 {
  font-size: 32px;
  font-weight: 600;
}

.markdown-body h2 {
  font-size: 24px;
  font-weight: 600;
}

.markdown-body h3 {
  font-size: 20px;
  font-weight: 600;
}

.markdown-body h4 {
  font-size: 16px;
  font-weight: 600;
}

.markdown-body h5 {
  font-size: 14px;
  font-weight: 600;
}

.markdown-body h6 {
  font-size: 12px;
  font-weight: 600;
}

.markdown-body p {
  margin-top: 0;
  margin-bottom: 10px;
}

.markdown-body blockquote {
  margin: 0;
}

.markdown-body ul,
.markdown-body ol {
  padding-left: 0;
  margin-top: 0;
  margin-bottom: 0;
}

.markdown-body ol ol,
.markdown-body ul ol {
  list-style-type: lower-roman;
}

.markdown-body ul ul ol,
.markdown-body ul ol ol,
.markdown-body ol ul ol,
.markdown-body ol ol ol {
  list-style-type: lower-alpha;
}

.markdown-body dd {
  margin-left: 0;
}

.markdown-body code {
  font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace;
  font-size: 12px;
}

.markdown-body pre {
  margin-top: 0;
  margin-bottom: 0;
  font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace;
  font-size: 12px;
}

.markdown-body .octicon {
  vertical-align: text-bottom;
}

.markdown-body .pl-0 {
  padding-left: 0 !important;
}

.markdown-body .pl-1 {
  padding-left: 4px !important;
}

.markdown-body .pl-2 {
  padding-left: 8px !important;
}

.markdown-body .pl-3 {
  padding-left: 16px !important;
}

.markdown-body .pl-4 {
  padding-left: 24px !important;
}

.markdown-body .pl-5 {
  padding-left: 32px !important;
}

.markdown-body .pl-6 {
  padding-left: 40px !important;
}

.markdown-body::before {
  display: table;
  content: "";
}

.markdown-body::after {
  display: table;
  clear: both;
  content: "";
}

.markdown-body>*:first-child {
  margin-top: 0 !important;
}

.markdown-body>*:last-child {
  margin-bottom: 0 !important;
}

.markdown-body a:not([href]) {
  color: inherit;
  text-decoration: none;
}

.markdown-body .anchor {
  float: left;
  padding-right: 4px;
  margin-left: -20px;
  line-height: 1;
}

.markdown-body .anchor:focus {
  outline: none;
}

.markdown-body p,
.markdown-body blockquote,
.markdown-body ul,
.markdown-body ol,
.markdown-body dl,
.markdown-body table,
.markdown-body pre {
  margin-top: 0;
  margin-bottom: 16px;
}

.markdown-body hr {
  height: 0.25em;
  padding: 0;
  margin: 24px 0;
  background-color: #e1e4e8;
  border: 0;
}

.markdown-body blockquote {
  padding: 0 1em;
  color: #6a737d;
  border-left: 0.25em solid #dfe2e5;
}

.markdown-body blockquote>:first-child {
  margin-top: 0;
}

.markdown-body blockquote>:last-child {
  margin-bottom: 0;
}

.markdown-body kbd {
  display: inline-block;
  padding: 3px 5px;
  font-size: 11px;
  line-height: 10px;
  color: #444d56;
  vertical-align: middle;
  background-color: #fafbfc;
  border: solid 1px #c6cbd1;
  border-bottom-color: #959da5;
  border-radius: 3px;
  box-shadow: inset 0 -1px 0 #959da5;
}

.markdown-body h1,
.markdown-body h2,
.markdown-body h3,
.markdown-body h4,
.markdown-body h5,
.markdown-body h6 {
  margin-top: 24px;
  margin-bottom: 16px;
  font-weight: 600;
  line-height: 1.25;
}

.markdown-body h1 .octicon-link,
.markdown-body h2 .octicon-link,
.markdown-body h3 .octicon-link,
.markdown-body h4 .octicon-link,
.markdown-body h5 .octicon-link,
.markdown-body h6 .octicon-link {
  color: #1b1f23;
  vertical-align: middle;
  visibility: hidden;
}

.markdown-body h1:hover .anchor,
.markdown-body h2:hover .anchor,
.markdown-body h3:hover .anchor,
.markdown-body h4:hover .anchor,
.markdown-body h5:hover .anchor,
.markdown-body h6:hover .anchor {
  text-decoration: none;
}

.markdown-body h1:hover .anchor .octicon-link,
.markdown-body h2:hover .anchor .octicon-link,
.markdown-body h3:hover .anchor .octicon-link,
.markdown-body h4:hover .anchor .octicon-link,
.markdown-body h5:hover .anchor .octicon-link,
.markdown-body h6:hover .anchor .octicon-link {
  visibility: visible;
}

.markdown-body h1 {
  padding-bottom: 0.3em;
  font-size: 2em;
  border-bottom: 1px solid #eaecef;
}

.markdown-body h2 {
  padding-bottom: 0.3em;
  font-size: 1.5em;
  border-bottom: 1px solid #eaecef;
}

.markdown-body h3 {
  font-size: 1.25em;
}

.markdown-body h4 {
  font-size: 1em;
}

.markdown-body h5 {
  font-size: 0.875em;
}

.markdown-body h6 {
  font-size: 0.85em;
  color: #6a737d;
}

.markdown-body ul,
.markdown-body ol {
  padding-left: 2em;
}

.markdown-body ul ul,
.markdown-body ul ol,
.markdown-body ol ol,
.markdown-body ol ul {
  margin-top: 0;
  margin-bottom: 0;
}

.markdown-body li>p {
  margin-top: 16px;
}

.markdown-body li+li {
  margin-top: 0.25em;
}

.markdown-body dl {
  padding: 0;
}

.markdown-body dl dt {
  padding: 0;
  margin-top: 16px;
  font-size: 1em;
  font-style: italic;
  font-weight: 600;
}

.markdown-body dl dd {
  padding: 0 16px;
  margin-bottom: 16px;
}

.markdown-body table {
  display: block;
  width: 100%;
  overflow: auto;
}

.markdown-body table th {
  font-weight: 600;
}

.markdown-body table th,
.markdown-body table td {
  padding: 6px 13px;
  border: 1px solid #dfe2e5;
}

.markdown-body table tr {
  background-color: #fff;
  border-top: 1px solid #c6cbd1;
}

.markdown-body table tr:nth-child(2n) {
  background-color: #f6f8fa;
}

.markdown-body img {
  max-width: 100%;
  box-sizing: content-box;
  background-color: #fff;
}

.markdown-body img[align=right] {
  padding-left: 20px;
}

.markdown-body img[align=left] {
  padding-right: 20px;
}

.markdown-body code {
  padding: 0;
  padding-top: 0.2em;
  padding-bottom: 0.2em;
  margin: 0;
  font-size: 85%;
  background-color: rgba(27,31,35,0.05);
  border-radius: 3px;
}

.markdown-body code::before,
.markdown-body code::after {
  letter-spacing: -0.2em;
  content: "\00a0";
}

.markdown-body pre {
  word-wrap: normal;
}

.markdown-body pre>code {
  padding: 0;
  margin: 0;
  font-size: 100%;
  word-break: normal;
  white-space: pre;
  background: transparent;
  border: 0;
}

.markdown-body .highlight {
  margin-bottom: 16px;
}

.markdown-body .highlight pre {
  margin-bottom: 0;
  word-break: normal;
}

.markdown-body .highlight pre,
.markdown-body pre {
  padding: 16px;
  overflow: auto;
  font-size: 85%;
  line-height: 1.45;
  background-color: #f6f8fa;
  border-radius: 3px;
}

.markdown-body pre code {
  display: inline;
  max-width: auto;
  padding: 0;
  margin: 0;
  overflow: visible;
  line-height: inherit;
  word-wrap: normal;
  background-color: transparent;
  border: 0;
}

.markdown-body pre code::before,
.markdown-body pre code::after {
  content: normal;
}

.markdown-body .full-commit .btn-outline:not(:disabled):hover {
  color: #005cc5;
  border-color: #005cc5;
}

.markdown-body kbd {
  display: inline-block;
  padding: 3px 5px;
  font: 11px "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace;
  line-height: 10px;
  color: #444d56;
  vertical-align: middle;
  background-color: #fafbfc;
  border: solid 1px #d1d5da;
  border-bottom-color: #c6cbd1;
  border-radius: 3px;
  box-shadow: inset 0 -1px 0 #c6cbd1;
}

.markdown-body :checked+.radio-label {
  position: relative;
  z-index: 1;
  border-color: #0366d6;
}

.markdown-body .task-list-item {
  list-style-type: none;
}

.markdown-body .task-list-item+.task-list-item {
  margin-top: 3px;
}

.markdown-body .task-list-item input {
  margin: 0 0.2em 0.25em -1.6em;
  vertical-align: middle;
}

.markdown-body hr {
  border-bottom-color: #eee;
}

</style>
