<?xml version="1.0"?>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
<meta content="Loggerhead/1.18.1 Python/2.6.5 Bazaar/2.5.1 Paste/1.7.2 PasteDeploy/1.3.3 SimpleTAL/4.1 Pygments/1.4 simplejson/2.1.3" name="generator" />
<title>~dolfin-core/dolfin/1.0.x : contents of demo/pde/navier-stokes/python/documentation.rst at revision 6546</title>
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
/<a href="/~dolfin-core/dolfin/1.0.x/files/6546/demo">demo</a>/<a href="/~dolfin-core/dolfin/1.0.x/files/6546/demo/pde">pde</a>/<a href="/~dolfin-core/dolfin/1.0.x/files/6546/demo/pde/navier-stokes">navier-stokes</a>/<a href="/~dolfin-core/dolfin/1.0.x/files/6546/demo/pde/navier-stokes/python">python</a>/documentation.rst
</span> (revision 6546)</span>
</div>

<div>

<ul id="submenuTabs">
<li id="first">
<a href="/~dolfin-core/dolfin/1.0.x/files/6546">browse files</a>
</li>
<li>
<a href="/~dolfin-core/dolfin/1.0.x/annotate/head:/demo/pde/navier-stokes/python/documentation.rst">view with revision information</a>
</li>

<li>
<a href="/~dolfin-core/dolfin/1.0.x/revision/6546">view revision</a>
</li>
<li>
<a href="/~dolfin-core/dolfin/1.0.x/changes?filter_file_id=documentation.rst-20110520162432-sqk259revj1v2oim-5">view changes to this file</a>
</li>
<li id="last">
<a href="/~dolfin-core/dolfin/1.0.x/download/head:/documentation.rst-20110520162432-sqk259revj1v2oim-5/documentation.rst">download file</a>
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
<a id="L142" href="#L142">142</a>
<a id="L143" href="#L143">143</a>
<a id="L144" href="#L144">144</a>
<a id="L145" href="#L145">145</a>
<a id="L146" href="#L146">146</a>
<a id="L147" href="#L147">147</a>
<a id="L148" href="#L148">148</a>
<a id="L149" href="#L149">149</a>
<a id="L150" href="#L150">150</a>
<a id="L151" href="#L151">151</a>
<a id="L152" href="#L152">152</a>
<a id="L153" href="#L153">153</a>
<a id="L154" href="#L154">154</a>
<a id="L155" href="#L155">155</a>
<a id="L156" href="#L156">156</a>
<a id="L157" href="#L157">157</a>
<a id="L158" href="#L158">158</a>
<a id="L159" href="#L159">159</a>
<a id="L160" href="#L160">160</a>
<a id="L161" href="#L161">161</a>
<a id="L162" href="#L162">162</a>
<a id="L163" href="#L163">163</a>
<a id="L164" href="#L164">164</a>
<a id="L165" href="#L165">165</a>
<a id="L166" href="#L166">166</a>
<a id="L167" href="#L167">167</a>
<a id="L168" href="#L168">168</a>
<a id="L169" href="#L169">169</a>
<a id="L170" href="#L170">170</a>
<a id="L171" href="#L171">171</a>
<a id="L172" href="#L172">172</a>
<a id="L173" href="#L173">173</a>
<a id="L174" href="#L174">174</a>
<a id="L175" href="#L175">175</a>
<a id="L176" href="#L176">176</a>
<a id="L177" href="#L177">177</a>
<a id="L178" href="#L178">178</a>
<a id="L179" href="#L179">179</a>
<a id="L180" href="#L180">180</a>
<a id="L181" href="#L181">181</a>
<a id="L182" href="#L182">182</a>
<a id="L183" href="#L183">183</a>
<a id="L184" href="#L184">184</a>
<a id="L185" href="#L185">185</a>
<a id="L186" href="#L186">186</a>
<a id="L187" href="#L187">187</a>
<a id="L188" href="#L188">188</a>
<a id="L189" href="#L189">189</a>
<a id="L190" href="#L190">190</a>
<a id="L191" href="#L191">191</a>
<a id="L192" href="#L192">192</a>
<a id="L193" href="#L193">193</a>
<a id="L194" href="#L194">194</a>
<a id="L195" href="#L195">195</a>
<a id="L196" href="#L196">196</a>
<a id="L197" href="#L197">197</a>
<a id="L198" href="#L198">198</a>
<a id="L199" href="#L199">199</a>
<a id="L200" href="#L200">200</a>
<a id="L201" href="#L201">201</a>
<a id="L202" href="#L202">202</a>
<a id="L203" href="#L203">203</a>
<a id="L204" href="#L204">204</a>
<a id="L205" href="#L205">205</a>
<a id="L206" href="#L206">206</a>
<a id="L207" href="#L207">207</a>
<a id="L208" href="#L208">208</a>
<a id="L209" href="#L209">209</a>
<a id="L210" href="#L210">210</a>
<a id="L211" href="#L211">211</a>
<a id="L212" href="#L212">212</a>
<a id="L213" href="#L213">213</a>
<a id="L214" href="#L214">214</a>
<a id="L215" href="#L215">215</a>
<a id="L216" href="#L216">216</a>
<a id="L217" href="#L217">217</a>
<a id="L218" href="#L218">218</a>
<a id="L219" href="#L219">219</a>
<a id="L220" href="#L220">220</a>
<a id="L221" href="#L221">221</a>
<a id="L222" href="#L222">222</a>
<a id="L223" href="#L223">223</a>
<a id="L224" href="#L224">224</a>
<a id="L225" href="#L225">225</a>
<a id="L226" href="#L226">226</a>
<a id="L227" href="#L227">227</a>
<a id="L228" href="#L228">228</a>
<a id="L229" href="#L229">229</a>
<a id="L230" href="#L230">230</a>
<a id="L231" href="#L231">231</a>
<a id="L232" href="#L232">232</a>
<a id="L233" href="#L233">233</a>
<a id="L234" href="#L234">234</a>
<a id="L235" href="#L235">235</a>
<a id="L236" href="#L236">236</a>
<a id="L237" href="#L237">237</a>
<a id="L238" href="#L238">238</a>
<a id="L239" href="#L239">239</a>
<a id="L240" href="#L240">240</a>
</pre>
</td>
<td class="viewCont">
<pre><span class="pyg-cp">.. Documentation for the incompressible Navier-Stokes demo from DOLFIN.</span>

<span class="pyg-p">..</span> <span class="pyg-nt">_demo_pde_navier_stokes_python_documentation:</span>

<span class="pyg-gh">Incompressible Navier-Stokes equations</span>
<span class="pyg-gh">======================================</span>

This demo is implemented in a single Python file,
<span class="pyg-na">:download:</span><span class="pyg-nv">`demo_navier-stokes.py`</span>, which contains both the variational
forms and the solver.

<span class="pyg-p">..</span> <span class="pyg-ow">include</span><span class="pyg-p">::</span> ../common.txt

<span class="pyg-gh">Implementation</span>
<span class="pyg-gh">--------------</span>

This demo is implemented in the <span class="pyg-na">:download:</span><span class="pyg-nv">`demo_navier-stokes.py`</span> file.

First, the <span class="pyg-na">:py:mod:</span><span class="pyg-nv">`dolfin`</span> module is imported:

<span class="pyg-p">..</span> <span class="pyg-ow">code-block</span><span class="pyg-p">::</span> python

    from dolfin import *

For the parallel case, we turn off log messages from processes other than
the the root process to avoid excessive output:

<span class="pyg-p">..</span> <span class="pyg-ow">code-block</span><span class="pyg-p">::</span> python

    # Print log messages only from the root process in parallel
    parameters[&quot;std_out_all_processes&quot;] = False;

We then load the mesh for the L-shaped domain from file:

<span class="pyg-p">..</span> <span class="pyg-ow">code-block</span><span class="pyg-p">::</span> python

    # Load mesh from file
    mesh = Mesh(&quot;lshape.xml.gz&quot;)

We next define a pair of function spaces <span class="pyg-na">:math:</span><span class="pyg-nv">`V`</span> and <span class="pyg-na">:math:</span><span class="pyg-nv">`Q`</span> for
the velocity and pressure, and trial and test functions on these
spaces:

<span class="pyg-p">..</span> <span class="pyg-ow">code-block</span><span class="pyg-p">::</span> python

    # Define function spaces (P2-P1)
    V = VectorFunctionSpace(mesh, &quot;CG&quot;, 2)
    Q = FunctionSpace(mesh, &quot;CG&quot;, 1)

    # Define trial and test functions
    u = TrialFunction(V)
    p = TrialFunction(Q)
    v = TestFunction(V)
    q = TestFunction(Q)

The time step, the length of the time interval, and the kinematic
viscosity are defined by:

<span class="pyg-p">..</span> <span class="pyg-ow">code-block</span><span class="pyg-p">::</span> python

    # Set parameter values
    dt = 0.01
    T = 3
    nu = 0.01

The time-dependent pressure boundary condition can be defined using
the <span class="pyg-na">:py:class:</span><span class="pyg-nv">`Expression &lt;dolfin.functions.expression.Expression&gt;`</span>
class:

<span class="pyg-p">..</span> <span class="pyg-ow">code-block</span><span class="pyg-p">::</span> python

    # Define time-dependent pressure boundary condition
    p_in = Expression(&quot;sin(3.0*t)&quot;, t=0.0)

Note that the variable <span class="pyg-s">``t``</span> is not automatically updated during
time-stepping, so we must remember to manually update the value of the
current time in each time step.

We may now define the boundary conditions for the velocity and
pressure. We define one no-slip boundary condition for the velocity
and a pair of boundary conditions for the pressure at the inflow and
outflow boundaries:

<span class="pyg-p">..</span> <span class="pyg-ow">code-block</span><span class="pyg-p">::</span> python

    # Define boundary conditions
    noslip  = DirichletBC(V, (0, 0),
                          &quot;on_boundary &amp;&amp; \
                           (x[0] &lt; DOLFIN_EPS | x[1] &lt; DOLFIN_EPS | \
                           (x[0] &gt; 0.5 - DOLFIN_EPS &amp;&amp; x[1] &gt; 0.5 - DOLFIN_EPS))&quot;)
    inflow  = DirichletBC(Q, p_in, &quot;x[1] &gt; 1.0 - DOLFIN_EPS&quot;)
    outflow = DirichletBC(Q, 0, &quot;x[0] &gt; 1.0 - DOLFIN_EPS&quot;)
    bcu = [noslip]
    bcp = [inflow, outflow]


We collect the boundary conditions in the two lists <span class="pyg-s">``bcu``</span> and
<span class="pyg-s">``bcp``</span> so that we may easily iterate over them below when we apply
the boundary conditions. This makes it easy to add new boundary
conditions or use this demo program to solve the Navier-Stokes
equations on other geometries.

We next define the functions and the coefficients that will be used
below:

<span class="pyg-p">..</span> <span class="pyg-ow">code-block</span><span class="pyg-p">::</span> python

    # Create functions
    u0 = Function(V)
    u1 = Function(V)
    p1 = Function(Q)

    # Define coefficients
    k = Constant(dt)
    f = Constant((0, 0))

Note that one may use the time step <span class="pyg-s">``dt``</span> directly in the
form. However, by using the :py:class:`Constant
<span class="pyg-nt">&lt;dolfin.functions.constant.Constant&gt;</span>` class, we may freely change the
size of the time step without triggering regeneration of code.

The next step is now to define the variational problems for the three
steps of Chorin&#39;s method. We do this by defining a pair of bilinear
and linear forms for each step:

<span class="pyg-p">..</span> <span class="pyg-ow">code-block</span><span class="pyg-p">::</span> python

    # Tentative velocity step
    F1 = (1/k)<span class="pyg-ge">*inner(u - u0, v)*</span>dx + inner(grad(u0)<span class="pyg-ge">*u0, v)*</span>dx + \
         nu<span class="pyg-ge">*inner(grad(u), grad(v))*</span>dx - inner(f, v)*dx
    a1 = lhs(F1)
    L1 = rhs(F1)

    # Pressure update
    a2 = inner(grad(p), grad(q))*dx
    L2 = -(1/k)<span class="pyg-ge">*div(u1)*</span>q*dx

    # Velocity update
    a3 = inner(u, v)*dx
    L3 = inner(u1, v)<span class="pyg-ge">*dx - k*</span>inner(grad(p1), v)*dx

Since the bilinear forms do not depend on any coefficients that change
during time-stepping, the corresponding matrices remain constant. We
may therefore assemble these before the time-stepping begins:

<span class="pyg-p">..</span> <span class="pyg-ow">code-block</span><span class="pyg-p">::</span> python

    # Assemble matrices
    A1 = assemble(a1)
    A2 = assemble(a2)
    A3 = assemble(a3)

    # Use amg preconditioner if available
    prec = &quot;amg&quot; if has_krylov_solver_preconditioner(&quot;amg&quot;) else &quot;default&quot;

During time-stepping, we will store the solution in VTK format
(readable by MayaVi and Paraview). We therefore create a pair of files
that can be used to store the solution. Specifying the <span class="pyg-s">``.pvd``</span> suffix
signals that the solution should be stored in VTK format:

<span class="pyg-p">..</span> <span class="pyg-ow">code-block</span><span class="pyg-p">::</span> python

    # Create files for storing solution
    ufile = File(&quot;results/velocity.pvd&quot;)
    pfile = File(&quot;results/pressure.pvd&quot;)

The time-stepping loop is now implemented as follows:

<span class="pyg-p">..</span> <span class="pyg-ow">code-block</span><span class="pyg-p">::</span> python

    # Time-stepping
    t = dt
    while t &lt; T + DOLFIN_EPS:

        # Update pressure boundary condition
        p_in.t = t

We remember to update the current time for the time-dependent pressure
boundary value.

For each of the three steps of Chorin&#39;s method, we assemble the
right-hand side, apply boundary conditions and solve a linear
system. Note the different use of preconditioners. Incomplete LU
factorization is used for the computation of the tentative velocity
and the velocity update, while algebraic multigrid is used for the
pressure equation if available:

<span class="pyg-p">..</span> <span class="pyg-ow">code-block</span><span class="pyg-p">::</span> python

    # Compute tentative velocity step
    begin(&quot;Computing tentative velocity&quot;)
    b1 = assemble(L1)
    [bc.apply(A1, b1) for bc in bcu]
    solve(A1, u1.vector(), b1, &quot;gmres&quot;, &quot;default&quot;)
    end()

    # Pressure correction
    begin(&quot;Computing pressure correction&quot;)
    b2 = assemble(L2)
    [bc.apply(A2, b2) for bc in bcp]
    solve(A2, p1.vector(), b2, &quot;gmres&quot;, prec)
    end()

    # Velocity correction
    begin(&quot;Computing velocity correction&quot;)
    b3 = assemble(L3)
    [bc.apply(A3, b3) for bc in bcu]
    solve(A3, u1.vector(), b3, &quot;gmres&quot;, &quot;default&quot;)
    end()

Note the use of <span class="pyg-s">``begin``</span> and <span class="pyg-s">``end``</span>; these improve the readability
of the output from the program by adding indentation to diagnostic
messages.

At the end of the time-stepping loop, we plot the solution, store the
solution to file, and update values for the next time step:

<span class="pyg-p">..</span> <span class="pyg-ow">code-block</span><span class="pyg-p">::</span> python

   # Plot solution
   plot(p1, title=&quot;Pressure&quot;, rescale=True)
   plot(u1, title=&quot;Velocity&quot;, rescale=True)

   # Save to file
   ufile &lt;&lt; u1
   pfile &lt;&lt; p1

   # Move to next time step
   u0.assign(u1)
   t += dt

Finally, we call the <span class="pyg-s">``interactive``</span> function to signal that the plot
window should be kept open and allow us to interact with (zoom,
rotate) the solution.

<span class="pyg-gh">Complete code</span>
<span class="pyg-gh">-------------</span>

<span class="pyg-p">..</span> <span class="pyg-ow">literalinclude</span><span class="pyg-p">::</span> demo_navier-stokes.py
   :start-after: # Begin demo
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