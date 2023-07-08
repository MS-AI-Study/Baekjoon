l=[]
for i in range(20):
    l.append(list(map(str,input().split(" "))))
t={"A+":4.5,"A0":4.0,"B+":3.5,"B0":3.0,"C+":2.5,"C0":2.0,"D+":1.5,"D0":1.0,"F":0.0}
g,s=0,0
for i in range(len(l)):
    if l[i][2]!="P":
        s+=float(l[i][1])
        g+=float(l[i][1])*t[l[i][2]]
print(g/s)


# "ObjectOrientedProgramming1 3.0 A+ IntroductiontoComputerEngineering 3.0 A+ ObjectOrientedProgramming2 3.0 A0 CreativeComputerEngineeringDesign 3.0 A+ AssemblyLanguage 3.0 A+ InternetProgramming 3.0 B0 ApplicationProgramminginJava 3.0 A0 SystemProgramming 3.0 B0 OperatingSystem 3.0 B0 WirelessCommunicationsandNetworking 3.0 C+ LogicCircuits 3.0 B0 DataStructure 4.0 A+ MicroprocessorApplication 3.0 B+ EmbeddedSoftware 3.0 C0 ComputerSecurity 3.0 D+ Database 3.0 C+ Algorithm 3.0 B0 CapstoneDesigninCSE 3.0 B+ CompilerDesign 3.0 D0 ProblemSolving 4.0 P"
# "BruteForce 3.0 F Greedy 1.0 F DivideandConquer 2.0 F DynamicProgramming 3.0 F DepthFirstSearch 4.0 F BreadthFirstSearch 3.0 F ShortestPath 4.0 F DisjointSet 2.0 F MinimumSpanningTree 2.0 F TopologicalSorting 1.0 F LeastCommonAncestor 2.0 F SegmentTree 4.0 F EulerTourTechnique 3.0 F StronglyConnectedComponent 2.0 F BipartiteMatching 2.0 F MaximumFlowProblem 3.0 F SuffixArray 1.0 F HeavyLightDecomposition 4.0 F CentroidDecomposition 3.0 F SplayTree 1.0 F"