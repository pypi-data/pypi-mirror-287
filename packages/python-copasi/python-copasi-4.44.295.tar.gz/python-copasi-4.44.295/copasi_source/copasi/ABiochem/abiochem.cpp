// Copyright (C) 2019 by Pedro Mendes, Rector and Visitors of the
// University of Virginia, University of Heidelberg, and University
// of Connecticut School of Medicine.
// All rights reserved.

// Copyright (C) 2017 - 2018 by Pedro Mendes, Virginia Tech Intellectual
// Properties, Inc., University of Heidelberg, and University of
// of Connecticut School of Medicine.
// All rights reserved.

// Copyright (C) 2010 - 2016 by Pedro Mendes, Virginia Tech Intellectual
// Properties, Inc., University of Heidelberg, and The University
// of Manchester.
// All rights reserved.

// Copyright (C) 2008 - 2009 by Pedro Mendes, Virginia Tech Intellectual
// Properties, Inc., EML Research, gGmbH, University of Heidelberg,
// and The University of Manchester.
// All rights reserved.

// Copyright (C) 2002 - 2007 by Pedro Mendes, Virginia Tech Intellectual
// Properties, Inc. and EML Research, gGmbH.
// All rights reserved.

/**
 *  ABiochem
 *
 *  This contains the common code for all network generators
 *  writen by Pedro Mendes, September 2002
 */

#define COPASI_MAIN // needed for anything with a main()

#include "copasi/copasi.h"

#include <iostream>
#include <fstream>
#include <string>
#include <strstream>
#include <vector>
#include <stack>
#include <queue>
#include <iomanip>
#include <algorithm>
#include <stdio.h>
#include <time.h>

// #include "tnt/tnt.h"
// #include "tnt/cmat.h"

#include "copasi/utilities/readwrite.h"
#include "copasi/elementaryFluxModes/CElementaryFluxModes.h"
#include "copasi/model/model.h"
#include "copasi/model/CSpec2Model.h"
#include "copasi/output/output.h"
#include "copasi/function/CFunctionDB.h"
// #include "copasi/trajectory/trajectory.h"
#include "copasi/steadystate/CEigen.h"
#include "copasi/utilities/CGlobals.h"
#include "copasi/utilities/CMethodParameter.h"
#include "ABiochem/clo.h"
#include "ABiochem/CGene.h"
#include "ABiochem/ABiochem.h"

extern "C" void r250_init(int seed);
extern "C" unsigned int r250n(unsigned n);
extern "C" double dr250();

extern char versionString[];

#define LARGE_GRAPH 1500

using namespace std;

void WriteDot(char *Title, CDataVector < CGene > &gene)
{
  unsigned C_INT32 i;
  C_INT32 j;
  char strtmp[1024];
  ofstream fout;

  sprintf(strtmp, "%s.dot", Title);
  fout.open(strtmp, ios::out);
  // dot file header
  fout << "digraph \"" << Title << "\" {\n";
  fout << "\tgraph\n\t[\n";
  fout << "\t\tcenter=\"true\"\n";
  fout << "\t\toverlap=\"false\"\n";
  fout << "\t\tDamping=0.999\n";
  fout << "\t\tfontname=\"Helvetica\"\n";
  fout << "\t\tmaxiter=1000000\n";
  fout << "\t\tsplines=\"true\"\n";
  fout << "\t\tsep=0.8\n";
  fout << "\t\tepsilon=0.0000001\n";
  fout << "\t\tlabel=\"" << Title << "\"\n";
  fout << "\t\tratio=\"auto\"\n";
  fout << "\t]\n\n";
  fout << "\tnode\n\t[\n";
  fout << "\t\tfontsize=9\n";
  fout << "\t\tfontname=\"Helvetica-bold\"\n";
  fout << "\t\tshape=\"circle\"\n";
  fout << "\t\tstyle=\"bold\"\n";
  fout << "\t]\n\n";
  fout << "\tedge\n\t[\n";
  fout << "\t\tfontsize=9\n";
  fout << "\t\tfontname=\"Helvetica\"\n";
  fout << "\t\tcolor=\"blue\"\n";
  fout << "\t\tarrowhead=\"normal\"\n";

  if (gene.size() < 15)
    fout << "\t\tstyle=\"bold\"\n";

  fout << "\t\tlen=2.5\n";
  fout << "\t]\n\n";

  // graph description
  for (i = 0; i < gene.size(); i++)
    for (j = 0; j < gene[i]->getModifierNumber(); j++)
      {
        fout << "\t" << gene[i]->getModifier(j)->getName() << " -> " << gene[i]->getName() << endl;

        if (gene[i]->getModifierType(j) == 0)
          fout << "\t\t[arrowhead=\"tee\"\n\t\tcolor=\"red\"]" << endl;
      }

  fout << "\n}";
  fout.close();
}

void WritePajek(char *Title, CDataVector < CGene > &gene)
{
  C_INT32 i, j, l, size;
  char strtmp[1024];
  ofstream fout;

  size = gene.size();
  sprintf(strtmp, "%s.net", Title);
  fout.open(strtmp, ios::out & ~ios::binary);
  fout << "*Network " << Title << endl;
  fout << "*Vertices " << size << endl;

  for (i = 0; i < size; i++)
    fout << i + 1 << " \"" << gene[i]->getName() << "\"" << endl;

  fout << "*Arcs" << endl;

  for (i = 0; i < size; i++)
    for (j = 0; j < gene[i]->getModifierNumber(); j++)
      for (l = 0; l < size; l++)
        if (gene[i]->getModifier(j) == gene[l])
          fout << l + 1 << " " << i + 1 << " 1 c " << (gene[i]->getModifierType(j) == 0 ? "Red" : "Blue") << endl;

  fout.close();
}

void WriteDistri(char *Title, CDataVector < CGene > &gene)
{
  C_INT32 i, size;
  char strtmp[1024];
  ofstream fout;
  vector <C_INT32> idegree, odegree, tdegree;

  size = gene.size();
  // create a vector to count all the degrees
  // there are N or less degrees
  // (this could be more efficient on memory done in a different way...)
  idegree.resize(size + 1);
  odegree.resize(size + 1);
  tdegree.resize(2 * (size + 1));

  for (i = 0; i <= size; i++)
    {
      idegree[i] = 0;
      odegree[i] = 0;
      tdegree[i] = 0;
    }

  for (i = size; i < 2 * (size + 1); i++)
    tdegree[i] = 0;

  // count over all genes
  for (i = 0; i < size; i++)
    {
      idegree[gene[i]->getInDegree()]++;
      odegree[gene[i]->getOutDegree()]++;
      tdegree[gene[i]->getTotalDegree()]++;
    }

  // now write the data in a gnuplot file
  sprintf(strtmp, "%s.distri.plt", Title);
  fout.open(strtmp, ios::out);
  //  fout << "set data style linespoints" << endl;
  fout << "set linestyle 1 lw 2\nset linestyle 2 lw 2\nset linestyle 3 lw 2" << endl;
  fout << "set title \'degree distribution for " << Title << "'" << endl;
  fout << "set xlabel \'# of links\'" << endl;
  fout << "set ylabel \'comulative distribution\'" << endl;
  fout << "plot \'-\' t \'in-degree\' ls 1, \'-\' t \'out-degree\' ls 2, \'-\' t \'all-degree\' ls 3" << endl;

  for (i = 0; i <= size; i++)
    fout << i << "\t" << idegree[i] << endl;

  fout << "e" << endl;

  for (i = 0; i <= size; i++)
    fout << i << "\t" << odegree[i] << endl;

  fout << "e" << endl;

  for (i = 0; i <= size; i++)
    fout << i << "\t" << tdegree[i] << endl;

  fout << "e" << endl;
  fout.close();
}

void MakeModel(char *Title, char *comments, CDataVector < CGene > &gene, C_INT32 n, C_INT32 k, CModel &model, C_INT32 specific)
{
  C_INT32 i, j, r, s, pos, neg;
  char strname[512], strname2[512], streq[512];
  string compname = "cell", rname, rchemeq, kiname;
  CReaction *react;
  std::vector <std::string> subnames;
  subnames.resize(1);
  // two reactions per gene
  r = 2 * n;
  // set the title and comments
  model.setTitle(Title);
  model.setComments(comments);
  // add one compartment to the model
  model.addCompartment(compname, 1.0);

  // create one metabolite for each gene
  for (i = 0; i < n; i++)
    model.addMetabolite(gene[i]->getName(), compname, 1.0, 1);

  model.initializeMetabolites();

  // create two reactions for each gene
  for (i = 0; i < n; i++)
    {
      // transcription
      sprintf(strname, "%s synthesis", gene[i]->getName().data());
      sprintf(streq, "-> %s", gene[i]->getName().data());
      rname = strname;
      rchemeq = streq;
      react = new CReaction(rname);

      if (react == NULL)
        {
          fprintf(stderr, "Failed to create a CReaction object");
          abort();
        }

      react->setChemEq(streq);
      s = gene[i]->getModifierNumber();

      for (j = 0; j < s; j++)
        {
          react->addModifier(gene[i]->getModifier(j)->getName());
        }

      if (specific)
        sprintf(strname, "basal %ld inh %ld spec act (indp)", gene[i]->getNegativeModifiers(),
                gene[i]->getPositiveModifiers());
      else
        sprintf(strname, "transcr %ld inh %ld act (indp)", gene[i]->getNegativeModifiers(),
                gene[i]->getPositiveModifiers());

      kiname = strname;
      react->setFunction(kiname);

      for (j = 0, pos = 1; j < s; j++)
        {
          if (gene[i]->getModifierType(j) == 1)
            {
              sprintf(strname, "A%ld", pos++);
              react->setParameterMapping(strname, gene[i]->getModifier(j)->getName());
            }
        }

      for (j = 0, neg = 1; j < s; j++)
        {
          if (gene[i]->getModifierType(j) == 0)
            {
              sprintf(strname, "I%ld", neg++);
              react->setParameterMapping(strname, gene[i]->getModifier(j)->getName());
            }
        }

      // first the basal rate
      sprintf(strname, "V");
      react->setParameterValue(strname, gene[i]->getRate());

      // we have two more constants per modifier
      for (j = 0, pos = neg = 1; j < s; j++)
        {
          if (gene[i]->getModifierType(j) == 0)
            {
              sprintf(strname, "Ki%ld", neg);
              sprintf(strname2, "ni%ld", neg++);
            }
          else
            {
              sprintf(strname, "Ka%ld", pos);
              sprintf(strname2, "na%ld", pos++);
            }

          react->setParameterValue(strname, gene[i]->getK(j));
          react->setParameterValue(strname2, gene[i]->getn(j));
        }

      model.addReaction(*react);
      // mRNA degradation
      sprintf(strname, "%s degradation", gene[i]->getName().data());
      sprintf(streq, "%s ->", gene[i]->getName().data());
      rname = strname;
      rchemeq = streq;
      react = new CReaction(rname);

      if (react == NULL)
        {
          fprintf(stderr, "Failed to create a CReaction object");
          abort();
        }

      react->setChemEq(streq);
      kiname = "Mass action (irreversible)";
      react->setFunction(kiname);
      // first the kinetic constant
      sprintf(strname, "k1");
      react->setParameterValue(strname, gene[i]->getDegradationRate());
      // now the substrate
      sprintf(strname, "substrate_0");
      subnames[0] = gene[i]->getName();
      react->setParameterMapping(strname, subnames);
      model.addReaction(*react);
    }

  // structural analysis (moieties, etc.)
  model.compile();
}

void MakeKinType(CFunctionDB &db, C_INT32 k, C_INT32 p, C_INT32 specific)
{
  C_INT32 i, j;
  CKinFunction *funct;
  char tmpstr[2048];
  string kiname, pname;
  string equation;

  // make name
  if (specific)
    sprintf(tmpstr, "basal %ld inh %ld spec act (indp)", k - p, p);
  else
    sprintf(tmpstr, "transcr %ld inh %ld act (indp)", k - p, p);

  kiname = tmpstr;

  if (db.findFunction(kiname) == NULL)
    {
      // not yet in the DB, so add it
      funct = new CKinFunction();

      if (funct == NULL)
        return;

      funct->setName(kiname);
      funct->setReversible(TriFalse);
      equation = "V";

      if (specific)
        {
          for (i = 0, j = 1; i < p; i++, j++)
            {
              sprintf(tmpstr, "*(A%ld/(A%ld+Ka%ld))^na%ld", j, j, j, j);
              equation += tmpstr;
            }
        }
      else
        {
          for (i = 0, j = 1; i < p; i++, j++)
            {
              sprintf(tmpstr, "*(1+A%ld/(A%ld+Ka%ld))^na%ld", j, j, j, j);
              equation += tmpstr;
            }
        }

      for (j = 1; i < k; i++, j++)
        {
          sprintf(tmpstr, "*(Ki%ld/(I%ld+Ki%ld))^ni%ld", j, j, j, j);
          equation += tmpstr;
        }

      funct->setDescription(equation);
      funct->addUsage("SUBSTRATES", 0, CRange::NoRange);
      funct->addUsage("PRODUCTS", 1, CRange::NoRange);
      pname = "V";
      funct->addParameter(pname, CFunctionParameter::FLOAT64, "PARAMETER");

      for (i = 0, j = 1; i < p; i++, j++)
        {
          sprintf(tmpstr, "Ka%ld", j);
          pname = tmpstr;
          funct->addParameter(pname, CFunctionParameter::FLOAT64, "PARAMETER");
          sprintf(tmpstr, "na%ld", j);
          pname = tmpstr;
          funct->addParameter(pname, CFunctionParameter::FLOAT64, "PARAMETER");
          sprintf(tmpstr, "A%ld", j);
          pname = tmpstr;
          funct->addParameter(pname, CFunctionParameter::FLOAT64, "MODIFIER");
        }

      for (j = 1; i < k; i++, j++)
        {
          sprintf(tmpstr, "Ki%ld", j);
          pname = tmpstr;
          funct->addParameter(pname, CFunctionParameter::FLOAT64, "PARAMETER");
          sprintf(tmpstr, "ni%ld", j);
          pname = tmpstr;
          funct->addParameter(pname, CFunctionParameter::FLOAT64, "PARAMETER");
          sprintf(tmpstr, "I%ld", j);
          pname = tmpstr;
          funct->addParameter(pname, CFunctionParameter::FLOAT64, "MODIFIER");
        }

      funct->compile();
      db.add(*funct);
    }
}

// calculates the single source shortest-path for gene g
// it also stores all the shortest distances in the vector dist
C_INT32 SSSP(CDataVector < CGene > &gene, C_INT32 g, C_INT32 *dist)
{
  C_INT32 i, j, n, u, cnt, depth;
  vector < C_INT32 > *distList, *nextList, nbrs;

  n = gene.size();

  // set all distances to the maximum
  for (i = 0; i < n; i++)
    dist[i] = n;

  // check if valid gene index
  if (g >= n)
    return n;

  // distance to self is zero
  dist[g] = 0;
  cnt = 0;
  distList = new vector < C_INT32 >;
  distList->push_back(g);

  for (depth = 1; distList->size() > 0; depth++)
    {
      nextList = new vector < C_INT32 >;

      for (i = 0; i < distList->size(); i++)
        {
          // fill nbrs with the neighbors
          nbrs.clear();

          for (j = 0; j < gene[(*distList)[i]]->getModifierNumber(); j++)
            nbrs.push_back(gene[(*distList)[i]]->getModifierIndex(j));

          for (j = 0; j < nbrs.size(); j++)
            {
              u = nbrs[j];

              if (dist[u] == n)
                {
                  cnt++;
                  dist[u] = depth;
                  nextList->push_back(u);
                }
            }
        }

      delete distList;
      distList = nextList;
    }

  delete nextList;
  return cnt == n - 1 ? depth - 2 : n;
}

// calculates the betweeness centrality for each gene
// uses the algorithm of Brandes (J Math Sociol 25, 163-177, 2001)
void Betweeness(CDataVector < CGene > &gene, vector <C_FLOAT64> &b)
{
  C_INT32 i, n, s, tot, v, w;
  vector < C_INT32 > sigma, d;
  vector < C_FLOAT64 > delta;
  stack < C_INT32 > S;
  queue < C_INT32 > Q;
  typedef list < C_INT32 > INTLIST;
  vector < INTLIST* > P;

  n = gene.size();
  sigma.reserve(n);
  delta.reserve(n);
  d.reserve(n);
  P.reserve(n);

  for (i = 0; i < n; i++)
    P[i] = new INTLIST;

  // reset variables
  for (i = 0; i < n; i++)
    b[i] = 0.0;

  // iterate over all genes
  for (s = 0; s < n; s++)
    {
      // reset variables
      while (!S.empty())
        S.pop();

      while (!Q.empty())
        Q.pop();

      for (i = 0; i < n; i++)
        {
          sigma[i] = 0;
          d[i] = -1;

          if (!P[i]->empty())
            P[i]->clear();
        }

      sigma[s] = 1;
      d[s] = 1;
      // add s to queue
      Q.push(s);

      while (! Q.empty())
        {
          v = Q.front();
          Q.pop();
          S.push(v);
          tot = gene[v]->getModifierNumber();

          for (i = 0; i < tot; i++)
            {
              w = gene[v]->getModifierIndex(i);

              // w found for the first time?
              if (d[w] < 0)
                {
                  Q.push(w);
                  d[w] = d[v] + 1;
                }

              // shortest path to w via v?
              if (d[w] == d[v] + 1)
                {
                  sigma[w] += sigma[v];
                  P[w]->push_back(v);
                }
            }
        }

      for (i = 0; i < n; i++)
        delta[i] = 0.0;

      // S returns vertices in order of non-increasing distance from s
      while (!S.empty())
        {
          w = S.top();
          S.pop();
          INTLIST::iterator it;

          for (it = P[w]->begin(); it != P[w]->end(); it++)
            delta[*it] += sigma[*it] * (1 + delta[w]) / sigma[w];

          if (w != s)
            {
              C_FLOAT64 tmp = delta[w];
              b[w] += delta[w];
            }
        }
    }

  for (i = 0; i < n; i++)
    {
      // make the measures relative
      b[i] /= ((C_FLOAT64)n - 1.0) * ((C_FLOAT64)n - 2.0);
      // delete the lists allocated
      delete P[i];
    }
}

// calculates the clustering coefficient of gene g
C_FLOAT64 cluster(CDataVector < CGene > &gene, C_INT32 g)
{
  C_INT32 i, j, k, m, n, edges;
  CDataVector <CGene> neighbors;
  CGene *ptG;
  // create the neighborhood
  n = gene[g]->getModifierNumber();

  if (n <= 1)
    return 0.0;

  for (i = 0; i < n; i++)
    neighbors.add(gene[g]->getModifier(i));

  // count the number of links within the neighborhood
  for (edges = i = 0; i < n; i++)
    {
      // one neighbor at a time
      m = neighbors[i]->getModifierNumber();

      for (j = 0; j < m; j++)
        {
          // one modifier at a time
          ptG = neighbors[i]->getModifier(j);

          // increment if this modifier is in the neighborhood
          // but it is not itself
          if (ptG != neighbors[i])
            for (k = 0; k < n; k++)
              if (ptG == neighbors[k])
                edges++;
        }
    }

  return (C_FLOAT64) edges / (C_FLOAT64)(n * (n - 1));
}

void GraphMetrics(CDataVector < CGene > &gene, C_INT32 tedges, char *Title)
{
  C_INT32 i, j, k, l, n;
  CMatrix<C_FLOAT64> Adj;
  CEigen *eigen;
  C_FLOAT64 ssRes, *eigen_r, *eigen_i;
  C_INT32 **dist;
  ofstream fout;
  char fname[1024];
  vector <C_FLOAT64> mpl, tpl, b;
  C_FLOAT64 cpl, cl, cll, cbl, acc, density, netcl, tmp, tmp2, netbc;
  C_INT32 idcenter, odcenter, clcenter, diameter, id, od, bcenter;

  // open the file for statistics
  sprintf(fname, "%s.netstat", Title);
  fout.open(fname, ios::out & ~ios::binary);
  n = gene.size();
  density = (C_FLOAT64) tedges / (C_FLOAT64)(n * n);
  fout << "number of vertices\t" << n << endl;
  fout << "number of arcs\t" << tedges << endl;
  fout << "density\t" << density << endl;

#ifdef XXXX
  // create the adjacency matrix
  Adj.newsize(n, n);

  for (i = 0; i < n; i++)
    {
      for (j = 0; j < n; j++)
        Adj[j][i] = 0.0;

      for (l = 0; l < gene[i]->getModifierNumber(); l++)
        {
          for (j = 0; j < n; j++)
            if (gene[i]->getModifier(l) == gene[j])
              {
                Adj[j][i] = 1.0;
                // if(gene[i]->getModifierType(l) == 0) Adj[j][i] = -1.0;
                // else Adj[j][i] = 1.0;
                break;
              }
        }
    }

  // calculate its eigenvalues
  eigen = new CEigen();
  ssRes = 1e-9;
  eigen->CalcEigenvalues(ssRes, Adj);
  eigen_r = eigen->getEigen_r();
  eigen_i = eigen->getEigen_i();
  // TODO: linear regression on positive real parts
  delete eigen;
#endif

  if (n < LARGE_GRAPH)
    {
      // find the diameter
      diameter = 0;
      dist = new C_INT32 * [n];

      for (i = 0; i < n; i++)
        {
          dist[i] = new C_INT32[n];
          l = SSSP(gene, i, dist[i]);

          if (l > diameter)
            diameter = l;
        }

      fout << "diameter\t" << diameter << endl;
      // calculate total and mean path lengths
      mpl.reserve(n);

      for (i = 0; i < n; i++)
        {
          cpl = 0.0;

          for (j = 0; j < n; j++)
            cpl += dist[i][j];

          cll = (C_FLOAT64)(n - 1) / cpl;
          cpl /= n - 1;
          mpl.push_back(cpl);
          tpl.push_back(cll);
        }
    }

  // find the degree centers
  for (id = od = idcenter = odcenter = i = 0; i < n; i++)
    {
      k = gene[i]->getOutDegree();

      if (k > od)
        {
          odcenter = i;
          od = k;
        }

      k = gene[i]->getInDegree();

      if (k > id)
        {
          idcenter = i;
          id = k;
        }
    }

  cl = (C_FLOAT64) id / (C_FLOAT64)(n - 1);
  fout << "in-degree center\t" << gene[idcenter]->getName() << endl;
  fout << "center's in-degree\t" << id << endl;
  fout << "center's relative in-degree\t" << cl << endl;
  cl = (C_FLOAT64) od / (C_FLOAT64)(n - 1);
  fout << "out-degree center\t" << gene[odcenter]->getName() << endl;
  fout << "center's out-degree\t" << od << endl;
  fout << "center's relative out-degree\t" << cl << endl;

  if (n < LARGE_GRAPH)
    {
      // find the closeness center, degree centralization,
      // and closeness centralization
      for (cll = 0.0, clcenter = -1, i = 0; i < n; i++)
        {
          if (tpl[i] > cll)
            {
              cll = tpl[i];
              clcenter = i;
            }
        }

      for (netcl = 0.0, i = 0; i < n; i++)
        netcl += cll - tpl[i];

      netcl /= ((C_FLOAT64)n - 1.0) * ((C_FLOAT64)n - 2.0) / (2.0 * (C_FLOAT64)n - 3.0);
      fout << "closeness center\t" << gene[clcenter]->getName() << endl;
      fout << "center's relative closeness\t" << cll << endl;
      fout << "network closeness centralization\t" << netcl << endl;
      // calculate betweeness centralities
      b.reserve(n);
      Betweeness(gene, b);

      //
      for (cbl = 0.0, bcenter = 0, i = 0; i < n; i++)
        {
          if (b[i] > cbl)
            {
              cbl = b[i];
              bcenter = i;
            }
        }

      for (netbc = 0.0, i = 0; i < n; i++)
        netbc += cbl - b[i];

      fout << "betweenness center\t" << gene[bcenter]->getName() << endl;
      fout << "center's relative betweenness\t" << cbl << endl;
      fout << "network betweenness centralization\t" << netbc << endl;
      // calculate characteristic path length
      sort(mpl.begin(), mpl.end());

      if (n / 2 == 0)
        cpl = (mpl[n / 2] + mpl[1 + n / 2]) * 0.5;
      else
        cpl = mpl[n / 2];

      fout << "characteristic path length\t" << cpl << endl;

      // calculate clustering coefficients
      for (acc = 0.0, i = 0; i < n; i++)
        {
          tmp = cluster(gene, i);
          acc += tmp;
        }

      acc /= n;
      fout << "average clustering coefficient\t" << acc << endl;
    }

  fout.close();
}

void WriteGepasi(char *Title, CModel &model)
{
  string linein;
  linein.reserve(100);
  char strtmp[1024], mtitle[512];
  ofstream fout;
  CWriteConfig *modelBuff;
  C_INT32 i, nmetab;
  CDataVector< CMetab > Metab = model.getMetabolites();

  nmetab = model.getTotMetab();
  sprintf(mtitle, "%s.gps", Title);
  // first part of the file come from a template
  ifstream fin("template.gps");

  if (!fin.is_open())
    return;

  fout.open(mtitle, ios::out | ios::trunc);
  getline(fin, linein);

  do
    {
      fout << linein << endl;
      getline(fin, linein);
    }
  while (linein.find("ReportFile=") != 0);

  sprintf(strtmp, "ReportFile=%s.txt", Title);
  fout << strtmp << endl;
  sprintf(strtmp, "DynamicsFile=%s.dyn", Title);
  fout << strtmp << endl;
  sprintf(strtmp, "SSFile=%s.ss", Title);
  fout << strtmp << endl;
  //  fout.flush();
  fout.close();
  // output the model
  modelBuff = new CWriteConfig(mtitle, ios::app);
  model.saveOld(*modelBuff);
  delete modelBuff;

  // last part also comes from the template
  do
    {
      getline(fin, linein);
    }
  while (linein.find("PlotType=") != 0);

  fout.open(mtitle, ios::app);

  do
    {
      fout << linein << endl;
      getline(fin, linein);
    }
  while (linein.find("PlotXEntry=") != 0);

  // plot entries are coded dynamically (to plot all metabolites)
  fout << "PlotXEntry=0" << endl;
  sprintf(strtmp, "PlotYTotal=%ld\nPlotZTotal=1", nmetab);
  fout << strtmp << endl;

  for (i = 0; i < nmetab; i++)
    {
      sprintf(strtmp, "PlotY%ld=%ld", i, i + 1);
      fout << strtmp << endl;
    }

  fout << "PlotZ0=-1" << endl;

  do
    {
      getline(fin, linein);
    }
  while (linein.find("User-defined functions") != 0);

  do
    {
      fout << linein << endl;
      getline(fin, linein);
    }
  while (linein.find("Time-course output") != 0);

  // output entries are coded dynamically (to plot all metabolites)
  fout << "Time-course output" << endl;
  sprintf(strtmp, "Items=%ld\nTitle=time\nType=14", nmetab + 1);
  fout << strtmp << endl;

  for (i = 0; i < nmetab; i++)
    {
      sprintf(strtmp, "Title=[%s]t\nType=3\nI=%s", Metab[i]->getName().data(), Metab[i]->getName().data());
      fout << strtmp << endl;
    }

  fout << "Steady-state output" << endl;
  sprintf(strtmp, "Items=%ld", nmetab);
  fout << strtmp << endl;

  for (i = 0; i < nmetab; i++)
    {
      sprintf(strtmp, "Title=[%s]ss\nType=2\nI=%s", Metab[i]->getName().data(), Metab[i]->getName().data());
      fout << strtmp << endl;
    }

  fout << "Scan\nEnabled=0" << endl;
  sprintf(strtmp, "Dimension=%ld", nmetab);
  fout << strtmp << endl;

  // set initial concentrations on scan
  for (i = 0; i < nmetab; i++)
    {
      sprintf(strtmp, "Title=[%s]i\nType=1\nI=%s", Metab[i]->getName().data(), Metab[i]->getName().data());
      fout << strtmp << endl;
      fout << "Min=0.1\nMax=10.0\nDensity=10\nLog=1\nIndependent=";

      if (i == 0)
        fout << "1";
      else
        fout << "0";

      fout << "\nGrid=1" << endl;
    }

  do
    {
      getline(fin, linein);
    }
  while (linein.find("Parameter Links") != 0);

  do
    {
      fout << linein << endl;
      getline(fin, linein);
    }
  while (!fin.eof());

  fout.close();
  fin.close();
}

void WriteSBML(char *Title, CModel &model)
{
  char mtitle[2048];
  ofstream fout;

  sprintf(mtitle, "%s.xml", Title);
  fout.open(mtitle, ios::out | ios::trunc);
  // write the SBML !
  model.saveSBML(fout);
  fout.close();
}

void WriteCmdLine(CGlobals *Copasi, char *Title)
{
  char mtitle[2048];
  ofstream fout;
  string a;
  C_INT32 pos, i;

  sprintf(mtitle, "%s.cmd", Title);
  fout.open(mtitle, ios::out | ios::trunc);
  // write the SBML !
  a = Copasi->Arguments[0];
  pos = a.find_last_of('/');

  if (pos == string::npos)
    pos = a.find_last_of('\\');

  if (pos != string::npos)
    fout << a.substr(pos + 1, a.size() - pos);
  else
    fout << a;

  for (i = 1; i < Copasi->Arguments.size(); i++)
    fout << " " << Copasi->Arguments[i];

  fout << endl;
  fout.close();
}

C_INT main(C_INT argc, char *argv[])
{
  C_INT32 n, k, i, j, tot, seed, pos, specific;
  CDataVector < CGene > GeneList;
  string prefix, fdb;
  CModel model;
  C_FLOAT64 positive, interact, rewiring, coopval, rateval, constval;

  char NetTitle[512], comments[2048];

  CGeneModifier *test;
  test = new CGeneModifier;

  // parse command line
  try
    {
      clo::parser cmdl;
      cmdl.parse(argc, argv);
      // get options from command line parser
      const clo::options &options = cmdl.get_options();

      if (options.version)
        {
          std::cout << argv[0] << versionString << endl;
          std::cout << "Written by Pedro Mendes" << endl;
          std::cout << "Copyright (C) 2003 Virginia Polytechnic Institute and State University" << endl;
          return 0;
        }

      if (options.specific_activation) specific = 1; else specific = 0;

      seed = options.seed;
      tot = options.total;
      n = options.genes;
      k = options.inputs;
      prefix = options.prefix;
      positive = options.positive;
      interact = options.interaction;
      rewiring = options.rewire;
      coopval = options.coop;
      rateval = options.rates;
      constval = options.constants;
    }
  catch (clo::autoexcept &e)
    {
      switch (e.get_autothrow_id())
        {
          case clo::autothrow_help:
            std::cout << "Usage: " << argv[0] << " [options]" << endl;
            std::cout << e.what();
            return 0;
        }
    }
  catch (std::exception &e)
    {
      std::cout << argv[0] << ": " << e.what() << endl;
      return 1;
    }

  Copasi = new CGlobals;
  // set the Function DB filename to be in the directory of the executable
  fdb = argv[0];
  pos = fdb.find_last_of('/');

  if (pos == string::npos)
    pos = fdb.find_last_of('\\');

  if (pos != string::npos)
    {
      fdb = fdb.substr(0, pos + 1) + "FunctionDB.gps";
      Copasi->pFunctionDB->setFilename(fdb);
    }

  Copasi->setArguments(argc, argv);

  if (seed)
    r250_init(seed);
  else
    r250_init(((int) time(NULL)));

  //  else r250_init(((int) time(NULL)) | 12783579);

  // generate tot networks of n genes with k random outputs each
  for (i = 0; i < tot; i++)
    {
      // build the gene network
      MakeGeneNetwork(n, k, positive, rewiring, coopval, rateval, constval, GeneList, comments);

      // sort out the modifiers
      for (j = 0; j < n; j++) GeneList[j]->sortModifiers();

      sprintf(NetTitle, "%s%03ld", prefix.data(), i + 1);
      // write the command line used to generate this model
      WriteCmdLine(Copasi, NetTitle);

      // create appropriate kinetic types, only those
      // that are really needed for this model
      for (j = 0; j < n; j++)
        MakeKinType(*Copasi->pFunctionDB, GeneList[j]->getModifierNumber(), GeneList[j]->getPositiveModifiers(), specific);

      // calculate several metrics
      GraphMetrics(GeneList, k, NetTitle);
      // create graph files
      WriteDot(NetTitle, GeneList);
      WritePajek(NetTitle, GeneList);
      // create distribution graph file
      WriteDistri(NetTitle, GeneList);
      // create COPASI model
      MakeModel(NetTitle, comments, GeneList, n, k, model, specific);
      // save Gepasi model
      WriteGepasi(NetTitle, model);
      // save SBML file
      WriteSBML(NetTitle, model);
      // cleanup model and vectors
      model.cleanup();
      GeneList.cleanup();
    }

  delete Copasi;
  return 0;
}
