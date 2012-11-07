<?xml version="1.0"?>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
<meta content="Loggerhead/1.18.1 Python/2.6.5 Bazaar/2.5.1 Paste/1.7.2 PasteDeploy/1.3.3 SimpleTAL/4.1 Pygments/1.4 simplejson/2.1.3" name="generator" />
<title>~dolfin-core/dolfin/1.0.x : contents of demo/pde/navier-stokes/python/demo_navier-stokes.py at revision 6546</title>
<link href="/static/css/global.css" rel="stylesheet" />
<link href="/static/images/favicon.png" rel="shortcut icon" />

<script type="text/javascript">
var global_path = '/~dolfin-core/dolfin/1.0.x/';
var collapsed_icon_path = '/static/images/treeCollapsed.png';
var expanded_icon_path = '/static/images/treeExpanded.png';
</script>
<script src="/static/javascript/yui/build/yui/yui-min.js" type="text/javascript"></script>
<script src="/static/javascript/yui/build/oop/oop-min.js" type="text/javascript"></script>
<script src="/static/javascript/yui/build/event/event-min.js" type="text/javascript"></script>
<script src="/static/javascript/yui/build/attribute/attribute-min.js" type="text/javascript"></script>
<script src="/static/javascript/yui/build/base/base-min.js" type="text/javascript"></script>
<script src="/static/javascript/yui/build/dom/dom-min.js" type="text/javascript"></script>
<script src="/static/javascript/yui/build/node/node-min.js" type="text/javascript"></script>
<script src="/static/javascript/yui/build/anim/anim-min.js" type="text/javascript"></script>
<script src="/static/javascript/yui/build/io/io-base-min.js" type="text/javascript"></script>
<script src="/static/javascript/custom.js" type="text/javascript"></script>

<link href="/static/css/view.css" media="all" type="text/css" rel="stylesheet" />
<link href="/static/css/highlight.css" media="all" type="text/css" rel="stylesheet" />

</head>
<body class="public">



<div class="black-link">
<a href="https://code.launchpad.net/~dolfin-core/dolfin/1.0.x">
← Back to branch summary
</a>
</div>


<h1 class="branch-name">
~dolfin-core/dolfin/1.0.x
</h1>

<ul id="menuTabs">


<li><a href="/~dolfin-core/dolfin/1.0.x/changes" title="Changes">Changes</a></li>
<li><a href="/~dolfin-core/dolfin/1.0.x/files" title="Files" id="on">Files</a></li>

</ul>

<div id="loggerheadCont">
<div id="search_terms"></div>

<div id="breadcrumbs">

<a href="https://code.launchpad.net/~dolfin-core/dolfin/1.0.x">~dolfin-core/dolfin/1.0.x</a>


<span>: <span class="breadcrumb">
/<a href="/~dolfin-core/dolfin/1.0.x/files/6546/demo">demo</a>/<a href="/~dolfin-core/dolfin/1.0.x/files/6546/demo/pde">pde</a>/<a href="/~dolfin-core/dolfin/1.0.x/files/6546/demo/pde/navier-stokes">navier-stokes</a>/<a href="/~dolfin-core/dolfin/1.0.x/files/6546/demo/pde/navier-stokes/python">python</a>/demo_navier-stokes.py
</span> (revision 6546)</span>
</div>

<div>

<ul id="submenuTabs">
<li id="first">
<a href="/~dolfin-core/dolfin/1.0.x/files/6546">browse files</a>
</li>
<li>
<a href="/~dolfin-core/dolfin/1.0.x/annotate/head:/demo/pde/navier-stokes/python/demo_navier-stokes.py">view with revision information</a>
</li>

<li>
<a href="/~dolfin-core/dolfin/1.0.x/revision/6546">view revision</a>
</li>
<li>
<a href="/~dolfin-core/dolfin/1.0.x/changes?filter_file_id=demo.py-20100830211455-qsy5ptkectvwhisn-2">view changes to this file</a>
</li>
<li id="last">
<a href="/~dolfin-core/dolfin/1.0.x/download/head:/demo.py-20100830211455-qsy5ptkectvwhisn-2/demo_navier-stokes.py">download file</a>
</li>
</ul>
<div class="view">
<table id="logentries">

<tr>
<td class="viewLine">
<pre><a id="L1" href="#L1">1</a>
<a id="L2" href="#L2">2</a>
<a id="L3" href="#L3">3</a>
<a id="L4" href="#L4">4</a>
<a id="L5" href="#L5">5</a>
<a id="L6" href="#L6">6</a>
<a id="L7" href="#L7">7</a>
<a id="L8" href="#L8">8</a>
<a id="L9" href="#L9">9</a>
<a id="L10" href="#L10">10</a>
<a id="L11" href="#L11">11</a>
<a id="L12" href="#L12">12</a>
<a id="L13" href="#L13">13</a>
<a id="L14" href="#L14">14</a>
<a id="L15" href="#L15">15</a>
<a id="L16" href="#L16">16</a>
<a id="L17" href="#L17">17</a>
<a id="L18" href="#L18">18</a>
<a id="L19" href="#L19">19</a>
<a id="L20" href="#L20">20</a>
<a id="L21" href="#L21">21</a>
<a id="L22" href="#L22">22</a>
<a id="L23" href="#L23">23</a>
<a id="L24" href="#L24">24</a>
<a id="L25" href="#L25">25</a>
<a id="L26" href="#L26">26</a>
<a id="L27" href="#L27">27</a>
<a id="L28" href="#L28">28</a>
<a id="L29" href="#L29">29</a>
<a id="L30" href="#L30">30</a>
<a id="L31" href="#L31">31</a>
<a id="L32" href="#L32">32</a>
<a id="L33" href="#L33">33</a>
<a id="L34" href="#L34">34</a>
<a id="L35" href="#L35">35</a>
<a id="L36" href="#L36">36</a>
<a id="L37" href="#L37">37</a>
<a id="L38" href="#L38">38</a>
<a id="L39" href="#L39">39</a>
<a id="L40" href="#L40">40</a>
<a id="L41" href="#L41">41</a>
<a id="L42" href="#L42">42</a>
<a id="L43" href="#L43">43</a>
<a id="L44" href="#L44">44</a>
<a id="L45" href="#L45">45</a>
<a id="L46" href="#L46">46</a>
<a id="L47" href="#L47">47</a>
<a id="L48" href="#L48">48</a>
<a id="L49" href="#L49">49</a>
<a id="L50" href="#L50">50</a>
<a id="L51" href="#L51">51</a>
<a id="L52" href="#L52">52</a>
<a id="L53" href="#L53">53</a>
<a id="L54" href="#L54">54</a>
<a id="L55" href="#L55">55</a>
<a id="L56" href="#L56">56</a>
<a id="L57" href="#L57">57</a>
<a id="L58" href="#L58">58</a>
<a id="L59" href="#L59">59</a>
<a id="L60" href="#L60">60</a>
<a id="L61" href="#L61">61</a>
<a id="L62" href="#L62">62</a>
<a id="L63" href="#L63">63</a>
<a id="L64" href="#L64">64</a>
<a id="L65" href="#L65">65</a>
<a id="L66" href="#L66">66</a>
<a id="L67" href="#L67">67</a>
<a id="L68" href="#L68">68</a>
<a id="L69" href="#L69">69</a>
<a id="L70" href="#L70">70</a>
<a id="L71" href="#L71">71</a>
<a id="L72" href="#L72">72</a>
<a id="L73" href="#L73">73</a>
<a id="L74" href="#L74">74</a>
<a id="L75" href="#L75">75</a>
<a id="L76" href="#L76">76</a>
<a id="L77" href="#L77">77</a>
<a id="L78" href="#L78">78</a>
<a id="L79" href="#L79">79</a>
<a id="L80" href="#L80">80</a>
<a id="L81" href="#L81">81</a>
<a id="L82" href="#L82">82</a>
<a id="L83" href="#L83">83</a>
<a id="L84" href="#L84">84</a>
<a id="L85" href="#L85">85</a>
<a id="L86" href="#L86">86</a>
<a id="L87" href="#L87">87</a>
<a id="L88" href="#L88">88</a>
<a id="L89" href="#L89">89</a>
<a id="L90" href="#L90">90</a>
<a id="L91" href="#L91">91</a>
<a id="L92" href="#L92">92</a>
<a id="L93" href="#L93">93</a>
<a id="L94" href="#L94">94</a>
<a id="L95" href="#L95">95</a>
<a id="L96" href="#L96">96</a>
<a id="L97" href="#L97">97</a>
<a id="L98" href="#L98">98</a>
<a id="L99" href="#L99">99</a>
<a id="L100" href="#L100">100</a>
<a id="L101" href="#L101">101</a>
<a id="L102" href="#L102">102</a>
<a id="L103" href="#L103">103</a>
<a id="L104" href="#L104">104</a>
<a id="L105" href="#L105">105</a>
<a id="L106" href="#L106">106</a>
<a id="L107" href="#L107">107</a>
<a id="L108" href="#L108">108</a>
<a id="L109" href="#L109">109</a>
<a id="L110" href="#L110">110</a>
<a id="L111" href="#L111">111</a>
<a id="L112" href="#L112">112</a>
<a id="L113" href="#L113">113</a>
<a id="L114" href="#L114">114</a>
<a id="L115" href="#L115">115</a>
<a id="L116" href="#L116">116</a>
<a id="L117" href="#L117">117</a>
<a id="L118" href="#L118">118</a>
<a id="L119" href="#L119">119</a>
<a id="L120" href="#L120">120</a>
<a id="L121" href="#L121">121</a>
<a id="L122" href="#L122">122</a>
<a id="L123" href="#L123">123</a>
<a id="L124" href="#L124">124</a>
<a id="L125" href="#L125">125</a>
<a id="L126" href="#L126">126</a>
<a id="L127" href="#L127">127</a>
<a id="L128" href="#L128">128</a>
<a id="L129" href="#L129">129</a>
<a id="L130" href="#L130">130</a>
<a id="L131" href="#L131">131</a>
<a id="L132" href="#L132">132</a>
<a id="L133" href="#L133">133</a>
<a id="L134" href="#L134">134</a>
<a id="L135" href="#L135">135</a>
<a id="L136" href="#L136">136</a>
<a id="L137" href="#L137">137</a>
<a id="L138" href="#L138">138</a>
<a id="L139" href="#L139">139</a>
<a id="L140" href="#L140">140</a>
<a id="L141" href="#L141">141</a>
</pre>
</td>
<td class="viewCont">
<pre><span class="pyg-sd">&quot;&quot;&quot;This demo program solves the incompressible Navier-Stokes equations</span>
<span class="pyg-sd">on an L-shaped domain using Chorin&#39;s splitting method.&quot;&quot;&quot;</span>

<span class="pyg-c"># Copyright (C) 2010-2011 Anders Logg</span>
<span class="pyg-c">#</span>
<span class="pyg-c"># This file is part of DOLFIN.</span>
<span class="pyg-c">#</span>
<span class="pyg-c"># DOLFIN is free software: you can redistribute it and/or modify</span>
<span class="pyg-c"># it under the terms of the GNU Lesser General Public License as published by</span>
<span class="pyg-c"># the Free Software Foundation, either version 3 of the License, or</span>
<span class="pyg-c"># (at your option) any later version.</span>
<span class="pyg-c">#</span>
<span class="pyg-c"># DOLFIN is distributed in the hope that it will be useful,</span>
<span class="pyg-c"># but WITHOUT ANY WARRANTY; without even the implied warranty of</span>
<span class="pyg-c"># MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the</span>
<span class="pyg-c"># GNU Lesser General Public License for more details.</span>
<span class="pyg-c">#</span>
<span class="pyg-c"># You should have received a copy of the GNU Lesser General Public License</span>
<span class="pyg-c"># along with DOLFIN. If not, see &lt;http://www.gnu.org/licenses/&gt;.</span>
<span class="pyg-c">#</span>
<span class="pyg-c"># Modified by Mikael Mortensen 2011</span>
<span class="pyg-c">#</span>
<span class="pyg-c"># First added:  2010-08-30</span>
<span class="pyg-c"># Last changed: 2011-06-30</span>

<span class="pyg-c"># Begin demo</span>

<span class="pyg-kn">from</span> <span class="pyg-nn">dolfin</span> <span class="pyg-kn">import</span> <span class="pyg-o">*</span>

<span class="pyg-c"># Print log messages only from the root process in parallel</span>
<span class="pyg-n">parameters</span><span class="pyg-p">[</span><span class="pyg-s">&quot;std_out_all_processes&quot;</span><span class="pyg-p">]</span> <span class="pyg-o">=</span> <span class="pyg-bp">False</span><span class="pyg-p">;</span>

<span class="pyg-c"># Load mesh from file</span>
<span class="pyg-n">mesh</span> <span class="pyg-o">=</span> <span class="pyg-n">Mesh</span><span class="pyg-p">(</span><span class="pyg-s">&quot;lshape.xml.gz&quot;</span><span class="pyg-p">)</span>

<span class="pyg-c"># Define function spaces (P2-P1)</span>
<span class="pyg-n">V</span> <span class="pyg-o">=</span> <span class="pyg-n">VectorFunctionSpace</span><span class="pyg-p">(</span><span class="pyg-n">mesh</span><span class="pyg-p">,</span> <span class="pyg-s">&quot;CG&quot;</span><span class="pyg-p">,</span> <span class="pyg-mi">2</span><span class="pyg-p">)</span>
<span class="pyg-n">Q</span> <span class="pyg-o">=</span> <span class="pyg-n">FunctionSpace</span><span class="pyg-p">(</span><span class="pyg-n">mesh</span><span class="pyg-p">,</span> <span class="pyg-s">&quot;CG&quot;</span><span class="pyg-p">,</span> <span class="pyg-mi">1</span><span class="pyg-p">)</span>

<span class="pyg-c"># Define trial and test functions</span>
<span class="pyg-n">u</span> <span class="pyg-o">=</span> <span class="pyg-n">TrialFunction</span><span class="pyg-p">(</span><span class="pyg-n">V</span><span class="pyg-p">)</span>
<span class="pyg-n">p</span> <span class="pyg-o">=</span> <span class="pyg-n">TrialFunction</span><span class="pyg-p">(</span><span class="pyg-n">Q</span><span class="pyg-p">)</span>
<span class="pyg-n">v</span> <span class="pyg-o">=</span> <span class="pyg-n">TestFunction</span><span class="pyg-p">(</span><span class="pyg-n">V</span><span class="pyg-p">)</span>
<span class="pyg-n">q</span> <span class="pyg-o">=</span> <span class="pyg-n">TestFunction</span><span class="pyg-p">(</span><span class="pyg-n">Q</span><span class="pyg-p">)</span>

<span class="pyg-c"># Set parameter values</span>
<span class="pyg-n">dt</span> <span class="pyg-o">=</span> <span class="pyg-mf">0.01</span>
<span class="pyg-n">T</span> <span class="pyg-o">=</span> <span class="pyg-mi">3</span>
<span class="pyg-n">nu</span> <span class="pyg-o">=</span> <span class="pyg-mf">0.01</span>

<span class="pyg-c"># Define time-dependent pressure boundary condition</span>
<span class="pyg-n">p_in</span> <span class="pyg-o">=</span> <span class="pyg-n">Expression</span><span class="pyg-p">(</span><span class="pyg-s">&quot;sin(3.0*t)&quot;</span><span class="pyg-p">,</span> <span class="pyg-n">t</span><span class="pyg-o">=</span><span class="pyg-mf">0.0</span><span class="pyg-p">)</span>

<span class="pyg-c"># Define boundary conditions</span>
<span class="pyg-n">noslip</span>  <span class="pyg-o">=</span> <span class="pyg-n">DirichletBC</span><span class="pyg-p">(</span><span class="pyg-n">V</span><span class="pyg-p">,</span> <span class="pyg-p">(</span><span class="pyg-mi">0</span><span class="pyg-p">,</span> <span class="pyg-mi">0</span><span class="pyg-p">),</span>
                      <span class="pyg-s">&quot;on_boundary &amp;&amp; </span><span class="pyg-se">\</span>
<span class="pyg-s">                       (x[0] &lt; DOLFIN_EPS | x[1] &lt; DOLFIN_EPS | </span><span class="pyg-se">\</span>
<span class="pyg-s">                       (x[0] &gt; 0.5 - DOLFIN_EPS &amp;&amp; x[1] &gt; 0.5 - DOLFIN_EPS))&quot;</span><span class="pyg-p">)</span>
<span class="pyg-n">inflow</span>  <span class="pyg-o">=</span> <span class="pyg-n">DirichletBC</span><span class="pyg-p">(</span><span class="pyg-n">Q</span><span class="pyg-p">,</span> <span class="pyg-n">p_in</span><span class="pyg-p">,</span> <span class="pyg-s">&quot;x[1] &gt; 1.0 - DOLFIN_EPS&quot;</span><span class="pyg-p">)</span>
<span class="pyg-n">outflow</span> <span class="pyg-o">=</span> <span class="pyg-n">DirichletBC</span><span class="pyg-p">(</span><span class="pyg-n">Q</span><span class="pyg-p">,</span> <span class="pyg-mi">0</span><span class="pyg-p">,</span> <span class="pyg-s">&quot;x[0] &gt; 1.0 - DOLFIN_EPS&quot;</span><span class="pyg-p">)</span>
<span class="pyg-n">bcu</span> <span class="pyg-o">=</span> <span class="pyg-p">[</span><span class="pyg-n">noslip</span><span class="pyg-p">]</span>
<span class="pyg-n">bcp</span> <span class="pyg-o">=</span> <span class="pyg-p">[</span><span class="pyg-n">inflow</span><span class="pyg-p">,</span> <span class="pyg-n">outflow</span><span class="pyg-p">]</span>

<span class="pyg-c"># Create functions</span>
<span class="pyg-n">u0</span> <span class="pyg-o">=</span> <span class="pyg-n">Function</span><span class="pyg-p">(</span><span class="pyg-n">V</span><span class="pyg-p">)</span>
<span class="pyg-n">u1</span> <span class="pyg-o">=</span> <span class="pyg-n">Function</span><span class="pyg-p">(</span><span class="pyg-n">V</span><span class="pyg-p">)</span>
<span class="pyg-n">p1</span> <span class="pyg-o">=</span> <span class="pyg-n">Function</span><span class="pyg-p">(</span><span class="pyg-n">Q</span><span class="pyg-p">)</span>

<span class="pyg-c"># Define coefficients</span>
<span class="pyg-n">k</span> <span class="pyg-o">=</span> <span class="pyg-n">Constant</span><span class="pyg-p">(</span><span class="pyg-n">dt</span><span class="pyg-p">)</span>
<span class="pyg-n">f</span> <span class="pyg-o">=</span> <span class="pyg-n">Constant</span><span class="pyg-p">((</span><span class="pyg-mi">0</span><span class="pyg-p">,</span> <span class="pyg-mi">0</span><span class="pyg-p">))</span>

<span class="pyg-c"># Tentative velocity step</span>
<span class="pyg-n">F1</span> <span class="pyg-o">=</span> <span class="pyg-p">(</span><span class="pyg-mi">1</span><span class="pyg-o">/</span><span class="pyg-n">k</span><span class="pyg-p">)</span><span class="pyg-o">*</span><span class="pyg-n">inner</span><span class="pyg-p">(</span><span class="pyg-n">u</span> <span class="pyg-o">-</span> <span class="pyg-n">u0</span><span class="pyg-p">,</span> <span class="pyg-n">v</span><span class="pyg-p">)</span><span class="pyg-o">*</span><span class="pyg-n">dx</span> <span class="pyg-o">+</span> <span class="pyg-n">inner</span><span class="pyg-p">(</span><span class="pyg-n">grad</span><span class="pyg-p">(</span><span class="pyg-n">u0</span><span class="pyg-p">)</span><span class="pyg-o">*</span><span class="pyg-n">u0</span><span class="pyg-p">,</span> <span class="pyg-n">v</span><span class="pyg-p">)</span><span class="pyg-o">*</span><span class="pyg-n">dx</span> <span class="pyg-o">+</span> \
     <span class="pyg-n">nu</span><span class="pyg-o">*</span><span class="pyg-n">inner</span><span class="pyg-p">(</span><span class="pyg-n">grad</span><span class="pyg-p">(</span><span class="pyg-n">u</span><span class="pyg-p">),</span> <span class="pyg-n">grad</span><span class="pyg-p">(</span><span class="pyg-n">v</span><span class="pyg-p">))</span><span class="pyg-o">*</span><span class="pyg-n">dx</span> <span class="pyg-o">-</span> <span class="pyg-n">inner</span><span class="pyg-p">(</span><span class="pyg-n">f</span><span class="pyg-p">,</span> <span class="pyg-n">v</span><span class="pyg-p">)</span><span class="pyg-o">*</span><span class="pyg-n">dx</span>
<span class="pyg-n">a1</span> <span class="pyg-o">=</span> <span class="pyg-n">lhs</span><span class="pyg-p">(</span><span class="pyg-n">F1</span><span class="pyg-p">)</span>
<span class="pyg-n">L1</span> <span class="pyg-o">=</span> <span class="pyg-n">rhs</span><span class="pyg-p">(</span><span class="pyg-n">F1</span><span class="pyg-p">)</span>

<span class="pyg-c"># Pressure update</span>
<span class="pyg-n">a2</span> <span class="pyg-o">=</span> <span class="pyg-n">inner</span><span class="pyg-p">(</span><span class="pyg-n">grad</span><span class="pyg-p">(</span><span class="pyg-n">p</span><span class="pyg-p">),</span> <span class="pyg-n">grad</span><span class="pyg-p">(</span><span class="pyg-n">q</span><span class="pyg-p">))</span><span class="pyg-o">*</span><span class="pyg-n">dx</span>
<span class="pyg-n">L2</span> <span class="pyg-o">=</span> <span class="pyg-o">-</span><span class="pyg-p">(</span><span class="pyg-mi">1</span><span class="pyg-o">/</span><span class="pyg-n">k</span><span class="pyg-p">)</span><span class="pyg-o">*</span><span class="pyg-n">div</span><span class="pyg-p">(</span><span class="pyg-n">u1</span><span class="pyg-p">)</span><span class="pyg-o">*</span><span class="pyg-n">q</span><span class="pyg-o">*</span><span class="pyg-n">dx</span>

<span class="pyg-c"># Velocity update</span>
<span class="pyg-n">a3</span> <span class="pyg-o">=</span> <span class="pyg-n">inner</span><span class="pyg-p">(</span><span class="pyg-n">u</span><span class="pyg-p">,</span> <span class="pyg-n">v</span><span class="pyg-p">)</span><span class="pyg-o">*</span><span class="pyg-n">dx</span>
<span class="pyg-n">L3</span> <span class="pyg-o">=</span> <span class="pyg-n">inner</span><span class="pyg-p">(</span><span class="pyg-n">u1</span><span class="pyg-p">,</span> <span class="pyg-n">v</span><span class="pyg-p">)</span><span class="pyg-o">*</span><span class="pyg-n">dx</span> <span class="pyg-o">-</span> <span class="pyg-n">k</span><span class="pyg-o">*</span><span class="pyg-n">inner</span><span class="pyg-p">(</span><span class="pyg-n">grad</span><span class="pyg-p">(</span><span class="pyg-n">p1</span><span class="pyg-p">),</span> <span class="pyg-n">v</span><span class="pyg-p">)</span><span class="pyg-o">*</span><span class="pyg-n">dx</span>

<span class="pyg-c"># Assemble matrices</span>
<span class="pyg-n">A1</span> <span class="pyg-o">=</span> <span class="pyg-n">assemble</span><span class="pyg-p">(</span><span class="pyg-n">a1</span><span class="pyg-p">)</span>
<span class="pyg-n">A2</span> <span class="pyg-o">=</span> <span class="pyg-n">assemble</span><span class="pyg-p">(</span><span class="pyg-n">a2</span><span class="pyg-p">)</span>
<span class="pyg-n">A3</span> <span class="pyg-o">=</span> <span class="pyg-n">assemble</span><span class="pyg-p">(</span><span class="pyg-n">a3</span><span class="pyg-p">)</span>

<span class="pyg-c"># Use amg preconditioner if available</span>
<span class="pyg-n">prec</span> <span class="pyg-o">=</span> <span class="pyg-s">&quot;amg&quot;</span> <span class="pyg-k">if</span> <span class="pyg-n">has_krylov_solver_preconditioner</span><span class="pyg-p">(</span><span class="pyg-s">&quot;amg&quot;</span><span class="pyg-p">)</span> <span class="pyg-k">else</span> <span class="pyg-s">&quot;default&quot;</span>

<span class="pyg-c"># Create files for storing solution</span>
<span class="pyg-n">ufile</span> <span class="pyg-o">=</span> <span class="pyg-n">File</span><span class="pyg-p">(</span><span class="pyg-s">&quot;results/velocity.pvd&quot;</span><span class="pyg-p">)</span>
<span class="pyg-n">pfile</span> <span class="pyg-o">=</span> <span class="pyg-n">File</span><span class="pyg-p">(</span><span class="pyg-s">&quot;results/pressure.pvd&quot;</span><span class="pyg-p">)</span>

<span class="pyg-c"># Time-stepping</span>
<span class="pyg-n">t</span> <span class="pyg-o">=</span> <span class="pyg-n">dt</span>
<span class="pyg-k">while</span> <span class="pyg-n">t</span> <span class="pyg-o">&lt;</span> <span class="pyg-n">T</span> <span class="pyg-o">+</span> <span class="pyg-n">DOLFIN_EPS</span><span class="pyg-p">:</span>

    <span class="pyg-c"># Update pressure boundary condition</span>
    <span class="pyg-n">p_in</span><span class="pyg-o">.</span><span class="pyg-n">t</span> <span class="pyg-o">=</span> <span class="pyg-n">t</span>

    <span class="pyg-c"># Compute tentative velocity step</span>
    <span class="pyg-n">begin</span><span class="pyg-p">(</span><span class="pyg-s">&quot;Computing tentative velocity&quot;</span><span class="pyg-p">)</span>
    <span class="pyg-n">b1</span> <span class="pyg-o">=</span> <span class="pyg-n">assemble</span><span class="pyg-p">(</span><span class="pyg-n">L1</span><span class="pyg-p">)</span>
    <span class="pyg-p">[</span><span class="pyg-n">bc</span><span class="pyg-o">.</span><span class="pyg-n">apply</span><span class="pyg-p">(</span><span class="pyg-n">A1</span><span class="pyg-p">,</span> <span class="pyg-n">b1</span><span class="pyg-p">)</span> <span class="pyg-k">for</span> <span class="pyg-n">bc</span> <span class="pyg-ow">in</span> <span class="pyg-n">bcu</span><span class="pyg-p">]</span>
    <span class="pyg-n">solve</span><span class="pyg-p">(</span><span class="pyg-n">A1</span><span class="pyg-p">,</span> <span class="pyg-n">u1</span><span class="pyg-o">.</span><span class="pyg-n">vector</span><span class="pyg-p">(),</span> <span class="pyg-n">b1</span><span class="pyg-p">,</span> <span class="pyg-s">&quot;gmres&quot;</span><span class="pyg-p">,</span> <span class="pyg-s">&quot;default&quot;</span><span class="pyg-p">)</span>
    <span class="pyg-n">end</span><span class="pyg-p">()</span>

    <span class="pyg-c"># Pressure correction</span>
    <span class="pyg-n">begin</span><span class="pyg-p">(</span><span class="pyg-s">&quot;Computing pressure correction&quot;</span><span class="pyg-p">)</span>
    <span class="pyg-n">b2</span> <span class="pyg-o">=</span> <span class="pyg-n">assemble</span><span class="pyg-p">(</span><span class="pyg-n">L2</span><span class="pyg-p">)</span>
    <span class="pyg-p">[</span><span class="pyg-n">bc</span><span class="pyg-o">.</span><span class="pyg-n">apply</span><span class="pyg-p">(</span><span class="pyg-n">A2</span><span class="pyg-p">,</span> <span class="pyg-n">b2</span><span class="pyg-p">)</span> <span class="pyg-k">for</span> <span class="pyg-n">bc</span> <span class="pyg-ow">in</span> <span class="pyg-n">bcp</span><span class="pyg-p">]</span>
    <span class="pyg-n">solve</span><span class="pyg-p">(</span><span class="pyg-n">A2</span><span class="pyg-p">,</span> <span class="pyg-n">p1</span><span class="pyg-o">.</span><span class="pyg-n">vector</span><span class="pyg-p">(),</span> <span class="pyg-n">b2</span><span class="pyg-p">,</span> <span class="pyg-s">&quot;gmres&quot;</span><span class="pyg-p">,</span> <span class="pyg-n">prec</span><span class="pyg-p">)</span>
    <span class="pyg-n">end</span><span class="pyg-p">()</span>

    <span class="pyg-c"># Velocity correction</span>
    <span class="pyg-n">begin</span><span class="pyg-p">(</span><span class="pyg-s">&quot;Computing velocity correction&quot;</span><span class="pyg-p">)</span>
    <span class="pyg-n">b3</span> <span class="pyg-o">=</span> <span class="pyg-n">assemble</span><span class="pyg-p">(</span><span class="pyg-n">L3</span><span class="pyg-p">)</span>
    <span class="pyg-p">[</span><span class="pyg-n">bc</span><span class="pyg-o">.</span><span class="pyg-n">apply</span><span class="pyg-p">(</span><span class="pyg-n">A3</span><span class="pyg-p">,</span> <span class="pyg-n">b3</span><span class="pyg-p">)</span> <span class="pyg-k">for</span> <span class="pyg-n">bc</span> <span class="pyg-ow">in</span> <span class="pyg-n">bcu</span><span class="pyg-p">]</span>
    <span class="pyg-n">solve</span><span class="pyg-p">(</span><span class="pyg-n">A3</span><span class="pyg-p">,</span> <span class="pyg-n">u1</span><span class="pyg-o">.</span><span class="pyg-n">vector</span><span class="pyg-p">(),</span> <span class="pyg-n">b3</span><span class="pyg-p">,</span> <span class="pyg-s">&quot;gmres&quot;</span><span class="pyg-p">,</span> <span class="pyg-s">&quot;default&quot;</span><span class="pyg-p">)</span>
    <span class="pyg-n">end</span><span class="pyg-p">()</span>

    <span class="pyg-c"># Plot solution</span>
    <span class="pyg-n">plot</span><span class="pyg-p">(</span><span class="pyg-n">p1</span><span class="pyg-p">,</span> <span class="pyg-n">title</span><span class="pyg-o">=</span><span class="pyg-s">&quot;Pressure&quot;</span><span class="pyg-p">,</span> <span class="pyg-n">rescale</span><span class="pyg-o">=</span><span class="pyg-bp">True</span><span class="pyg-p">)</span>
    <span class="pyg-n">plot</span><span class="pyg-p">(</span><span class="pyg-n">u1</span><span class="pyg-p">,</span> <span class="pyg-n">title</span><span class="pyg-o">=</span><span class="pyg-s">&quot;Velocity&quot;</span><span class="pyg-p">,</span> <span class="pyg-n">rescale</span><span class="pyg-o">=</span><span class="pyg-bp">True</span><span class="pyg-p">)</span>

    <span class="pyg-c"># Save to file</span>
    <span class="pyg-n">ufile</span> <span class="pyg-o">&lt;&lt;</span> <span class="pyg-n">u1</span>
    <span class="pyg-n">pfile</span> <span class="pyg-o">&lt;&lt;</span> <span class="pyg-n">p1</span>

    <span class="pyg-c"># Move to next time step</span>
    <span class="pyg-n">u0</span><span class="pyg-o">.</span><span class="pyg-n">assign</span><span class="pyg-p">(</span><span class="pyg-n">u1</span><span class="pyg-p">)</span>
    <span class="pyg-n">t</span> <span class="pyg-o">+=</span> <span class="pyg-n">dt</span>
    <span class="pyg-k">print</span> <span class="pyg-s">&quot;t =&quot;</span><span class="pyg-p">,</span> <span class="pyg-n">t</span>

<span class="pyg-c"># Hold plot</span>
<span class="pyg-n">interactive</span><span class="pyg-p">()</span>
</pre>
</td>
</tr>
</table>
</div>
</div>
<p id="footer" class="fl">Loggerhead 1.18.1 is a web-based interface for <a href="http://bazaar-vcs.org/">Bazaar</a> branches</p>
</div>
</body>
</html>