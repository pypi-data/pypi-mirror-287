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
 *  CGene class.
 *  Written by Pedro Mendes September 2002.
 *
 *  For representing a gene and all the elements needed for COPASI
 *  to represent it in a model
 */

#ifdef WIN32
#pragma warning(disable : 4786)
#endif  // WIN32

#define  COPASI_TRACE_CONSTRUCTION
#include <iostream>
#include <string>
#include <vector>

#include "copasi/copasi.h"

#include "copasi/utilities/CGlobals.h"
#include "ABiochem/CGene.h"

CGeneModifier::CGeneModifier(const std::string & name,
                             CDataContainer * pParent):
  CDataObject(name, pParent, "CGeneModifier")
{
  mModifier = NULL;
  mType = 0;
  mK = 1.0;
}

CGeneModifier::CGeneModifier(const CGeneModifier & src,
                             CDataContainer * pParent):
  CDataObject(src, pParent)
{}

CGeneModifier::CGeneModifier(CGene * modf, C_INT32 type, C_FLOAT64 K, C_FLOAT64 n)
{
  mModifier = modf;

  if ((type >= 0) && (type < 2))
    mType = type;
  else
    type = 0;

  mK = K > 0.0 ? K : 1.0;
  mn = n > 0.0 ? n : 1.0;
}

CGeneModifier::~CGeneModifier()
{}

CGene * CGeneModifier::getModifier(void)
{
  return mModifier;
}

C_INT32 CGeneModifier::getType(void)
{
  return mType;
}

void CGeneModifier::setType(C_INT32 t)
{
  mType = t;
}

C_FLOAT64 CGeneModifier::getK(void)
{
  return mK;
}

C_FLOAT64 CGeneModifier::getn(void)
{
  return mn;
}

void CGeneModifier::cleanup()
{}

CGene::CGene(const std::string & name,
             CDataContainer * pParent):
  CDataObject(name, pParent, "CGene")
{
  mInDegree = 0;
  mOutDegree = 0;
  mRate = 1.0;
  mDegradationRate = 1.0;
}

CGene::CGene(const CGene & src,
             CDataContainer * pParent):
  CDataObject(src, pParent)
{}

CGene::~CGene()
{}

void CGene::setName(const std::string & name)
{
  mName = name;
}

const std::string & CGene::getName() const
{
  return mName;
}

C_INT32 CGene::getModifierNumber()
{
  //  return mModifier.size();
  return mInDegree;
}

CGene * CGene::getModifier(C_INT32 n)
{
  return mModifier[n]->getModifier();
}

void CGene::setRate(C_FLOAT64 rate)
{
  mRate = rate;
}

C_FLOAT64 CGene::getRate(void)
{
  return mRate;
}

void CGene::setDegradationRate(C_FLOAT64 rate)
{
  mDegradationRate = rate;
}

C_FLOAT64 CGene::getDegradationRate(void)
{
  return mDegradationRate;
}

void CGene::addModifier(CGene *modf, C_INT32 idx, C_INT32 type, C_FLOAT64 K, C_FLOAT64 n)
{
  CGeneModifier *temp;
  temp = new CGeneModifier(modf, type, K, n);
  // add the modifier object to the list
  mModifier.add(temp);
  // add the index to the list
  mModifierIndex.push_back(idx);
  // increment the in-degree of this gene
  addInDegree();
  // and the out-degree of the modifier's
  modf->addOutDegree();
}

void CGene::removeModifier(CGene *modf)
{
  C_INT32 i, j;
  C_INT32 *it;

  for (i = 0; i < getModifierNumber(); i++)
    if (modf == getModifier(i))
      {
        // decrement the in-degree of this gene
        decreaseInDegree();
        // and the out-degree of the modifier's
        modf->decreaseOutDegree();
        mModifier.remove(i);
        it = mModifierIndex.begin();

        for (j = 0; j < i; j++)
          it++;

        mModifierIndex.erase(it);
        return;
      }
}

C_INT32 CGene::getModifierIndex(C_INT32 n)
{
  return mModifierIndex[n];
}

C_INT32 CGene::getModifierType(C_INT32 n)
{
  return mModifier[n]->getType();
}

C_FLOAT64 CGene::getK(C_INT32 i)
{
  return mModifier[i]->getK();
}

C_FLOAT64 CGene::getn(C_INT32 i)
{
  return mModifier[i]->getn();
}

void CGene::cleanup()
{
  mModifier.cleanup();
}

C_INT32 CGene::getNegativeModifiers(void)
{
  C_INT32 i, n, s;
  s = mModifier.size();

  for (i = n = 0; i < s; i++)
    if (mModifier[i]->getType() == 0)
      n++;

  return n;
}

C_INT32 CGene::getPositiveModifiers(void)
{
  C_INT32 i, n, s;
  s = mModifier.size();

  for (i = n = 0; i < s; i++)
    if (mModifier[i]->getType() == 1)
      n++;

  return n;
}

C_INT32 CGene::getInDegree()
{
  return mInDegree;
}

void CGene::addInDegree()
{
  mInDegree++;
}

void CGene::decreaseInDegree()
{
  mInDegree--;
}

C_INT32 CGene::getOutDegree()
{
  return mOutDegree;
}

void CGene::addOutDegree()
{
  mOutDegree++;
}

void CGene::decreaseOutDegree()
{
  mOutDegree--;
}

C_INT32 CGene::getTotalDegree()
{
  return mOutDegree + mInDegree;
}

void CGene::sortModifiers()
{
  C_INT32 np, i, j;
  CGeneModifier *tempModf;
  C_INT32 tempK, tempN, tempIdx;
  np = getPositiveModifiers();

  for (i = 0, j = mInDegree - 1; i < np; i++)
    {
      if (mModifier[i]->getType() == 0)
        {
          // this is in the wrong place, find a positive one
          for (; j >= np; j--)
            {
              if (mModifier[j]->getType() == 1)
                {
                  // found one, let's swap
                  tempModf = mModifier[i];
                  tempIdx = getModifierIndex(i);
                  mModifier[i] = mModifier[j];
                  mModifierIndex[i] = mModifierIndex[j];
                  mModifier[i]->setType(1);
                  mModifier[j] = tempModf;
                  mModifierIndex[j] = tempIdx;
                  mModifier[j]->setType(0);
                  break;
                }
            }
        }
    }
}
