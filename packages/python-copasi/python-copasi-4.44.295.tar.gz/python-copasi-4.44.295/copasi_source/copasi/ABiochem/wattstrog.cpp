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
 *  ABiochem  -  wattstrog
 *
 *  A program to generate random gene networks
 *  following an Watts-Stroganz small-world topology
 *
 *  writen by Pedro Mendes, September 2002
 *  Biochemical Networks Modeling Group
 *  Virginia Bioinformatics Institute
 */

#define COPASI_TRACE_CONSTRUCTION
#include "copasi/copasi.h"
#include <stdio.h>
#include "copasi/utilities/CMethodParameter.h"
#include "copasi/model/model.h"
#include "ABiochem/CGene.h"

extern "C" void r250_init(int seed);
extern "C" unsigned int r250n(unsigned n);
extern "C" double dr250();

char versionString[] = " version 1.3";

using namespace std;

/**
 *  Creates a gene network using a small-world (watts-strogatz) topology
 *
 *  @param C_INT32 n the total number of genes
 *  @param C_INT32 k the total number of links
 *  @param C_FLOAT64 p the probability that a link is positive
 *  @param C_FLOAT64 r the probability of rewiring a gene
 *  @param C_FLOAT64 coopval the value for Hill coefficients
 *  @param C_FLOAT64 rateval the value for rate constants
 *  @param C_FLOAT64 constval the value for inh/act constants
 *  @param "CDataVector < CGene > &" gene a vector of genes (the network)
 *  @param "char *" comments a string to write comments on the network
 */

void MakeGeneNetwork(C_INT32 n,
                     C_INT32 k,
                     C_FLOAT64 p,
                     C_FLOAT64 r,
                     C_FLOAT64 coopval,
                     C_FLOAT64 rateval,
                     C_FLOAT64 constval,
                     CDataVector < CGene > &gene,
                     char *comments)
{
  C_INT32 i, j, l, l2, m, modf, links, links2;
  char gn[1024];

  // links accounts for the number of links per gene
  links = k / n;
  links2 = links / 2;
  // create and name genes
  gene.resize(n);

  for (i = 0; i < n; i++)
    {
      sprintf(gn, "G%ld", i + 1);
      gene[i]->setName(gn);
    }

  // create a regular 1-dimensional grid
  for (i = 0; i < n; i++) // each gene
    {
      for (j = 1; j <= links2; j++) // each link (one link each side)
        {
          l = i + j;

          if (l >= n)
            l %= n;

          l2 = i - j;

          if (l2 < 0)
            l2 = n + l2;

          // add the two links, i->l i->l2
          if (dr250() < p)
            modf = 1;
          else
            modf = 0;

          gene[i]->addModifier(gene[l], l, modf, constval, coopval);

          if (dr250() < p)
            modf = 1;
          else
            modf = 0;

          gene[i]->addModifier(gene[l2], l2, modf, constval, coopval);
        }

      gene[i]->setRate(rateval);
      gene[i]->setDegradationRate(rateval);
    }

  // now rewire the grid
  for (i = 1; i <= links2; i++) // each link (one link each side)
    {
      for (j = 0; j < n; j++) // each gene
        {
          l = j + i;

          if (l >= n)
            l %= n;

          l2 = j - i;

          if (l2 < 0)
            l2 = n + l2;

          // check if we rewire the l link
          if (dr250() < r)
            {
              // store the modifier type
              modf = 0;

              for (m = 0; m < gene[i]->getModifierNumber(); m++)
                if (gene[l] == gene[i]->getModifier(m))
                  modf = gene[i]->getModifierType(m);

              // remove the previous link
              gene[j]->removeModifier(gene[l]);

              // find a new link (that is not yet there)
              for (l = -1; l < 0;)
                {
                  l = r250n(n);

                  for (m = 0; m < gene[i]->getModifierNumber(); m++)
                    if (gene[l] == gene[i]->getModifier(m))
                      {
                        l = -1;
                        break;
                      }
                }

              // add the new link
              gene[j]->addModifier(gene[l], l, modf, constval, coopval);
            }

          // check if we rewire the l2 link
          if (dr250() < r)
            {
              // store the modifier type
              modf = 0;

              for (m = 0; m < gene[i]->getModifierNumber(); m++)
                if (gene[l2] == gene[i]->getModifier(m))
                  modf = gene[i]->getModifierType(m);

              // remove the previous link
              gene[j]->removeModifier(gene[l2]);

              // find a new link (that is not yet there)
              for (l2 = -1; l2 < 0;)
                {
                  l2 = r250n(n);

                  for (m = 0; m < gene[i]->getModifierNumber(); m++)
                    if (gene[l2] == gene[i]->getModifier(m))
                      {
                        l2 = -1;
                        break;
                      }
                }

              // add the new link
              gene[j]->addModifier(gene[l2], l2, modf, constval, coopval);
            }
        }
    }

  sprintf(comments, "Model of a small-world gene network using the Watts-Strogatz algorithm\nwith %ld genes, %ld total input connections, and probability of rewiring %lg.\n\nCreated automatically by the A-Biochem system", n, n * 2 * links2, r);
}
