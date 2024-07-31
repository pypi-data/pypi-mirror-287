// Copyright (C) 2017 by Pedro Mendes, Virginia Tech Intellectual
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

#ifndef COPASI_CGene
#define COPASI_CGene

#include <string>
#include <iostream>

#include "copasi/core/CDataVector.h"
#include "copasi/core/CDataObject.h"

class CGene;

class CGeneModifier: public CDataObject
{
  // Attributes

private:
  /**
   *  Modifier gene
   */
  CGene * mModifier;

  /**
   *  Type (0=Inhibition, 1=Activation)
   */
  C_INT32 mType;

  /**
   *  Inhibition/activation constant
   */
  C_FLOAT64 mK;

  /**
   *  Hill coefficient
   */
  C_FLOAT64 mn;

public:

  /**
   *  Default constructor
   */
  CGeneModifier(const std::string & name = "NoName",
                CDataContainer * pParent = NULL);
  CGeneModifier(const CGeneModifier & src,
                CDataContainer * pParent = NULL);

  /**
   *  Constructor
   *  @param modf pointer to CGene modifier.
   *  @param type (0=Inhibition, 1=Activation).
   *  @param K positive value for effect strength.
   */
  CGeneModifier(CGene * modf, C_INT32 type, C_FLOAT64 K, C_FLOAT64 n);

  /**
   *  Retrieves the pointer to the modifier
   */
  CGene * getModifier(void);

  /**
   *  Retrieves the type of modification
   */
  C_INT32 getType(void);

  /**
   *  Sets the type of the modification
   */
  void setType(C_INT32 t);

  /**
   *  Retrieves the inhibition/activation constant
   */
  C_FLOAT64 getK(void);

  /**
   *  Retrieves the Hill coefficient
   */
  C_FLOAT64 getn(void);

  /**
   *  Destructor
   */
  ~CGeneModifier();

  /**
   *  cleanup()
   */
  void cleanup();
};

class CGene: public CDataObject
{
  // Attributes

private:
  /**
   *  Name of the gene
   */
  std::string mName;

  /**
   *  Basal or maximal rate for the transcription
   */
  C_FLOAT64 mRate;

  /**
   *  Basal or maximal rate for the transcription
   */
  C_FLOAT64 mDegradationRate;

  /**
   *  number of incoming links to this gene
   */
  C_INT32 mInDegree;

  /**
   *  number of outgoing links from this gene
   */
  C_INT32 mOutDegree;

  /**
   *  List of other genes that modify transcription of this one
   *  @supplierCardinality 0..*
   *  @associates <{CGene*}>
   */
  CDataVector< CGeneModifier > mModifier;

  /**
   *  List of other genes that modify transcription of this one (indices)
   *  @supplierCardinality 0..*
   *  @associates <{C_INT32}>
   */
  std::vector < C_INT32 > mModifierIndex;

public:

  /**
   *  Default constructor
   */
  CGene(const std::string & name = "NoName",
        CDataContainer * pParent = NULL);
  CGene(const CGene & src,
        CDataContainer * pParent = NULL);

  /**
   *  Destructor
   */
  ~CGene();

  /**
   *  Sets the name of the gene.
   */
  void setName(const std::string & name);

  /**
   *  Retrieve the name of the gene.
   */
  const std::string & getName() const;

  /**
   *  Retrieve the number of modifiers.
   */
  C_INT32 getModifierNumber();

  /**
   *  Retrieve a Modifier.
   */
  CGene * getModifier(C_INT32 n);

  /**
   *  Sets the name of the gene.
   */
  void setRate(C_FLOAT64 rate);

  /**
   *  Retrieves the constant
   */
  C_FLOAT64 getDegradationRate(void);

  /**
   *  Sets the name of the gene.
   */
  void setDegradationRate(C_FLOAT64 rate);

  /**
   *  Retrieves the constant
   */
  C_FLOAT64 getRate(void);

  /**
   *  Add a new Modifier to this gene.
   */
  void addModifier(CGene *modf, C_INT32 idx, C_INT32 type, C_FLOAT64 K, C_FLOAT64 n);

  /**
   *  Removes a Modifier from this gene.
  *
  *  @param "CGene *" modf pointer to the modifier gene to remove
   */
  void removeModifier(CGene *modf);

  /**
   *  Retrieve the index of Modifier n.
   */
  C_INT32 getModifierIndex(C_INT32 n);

  /**
   *  Retrieve the type of Modifier n.
   */
  C_INT32 getModifierType(C_INT32 n);

  /**
   *  Retrieve the inhibition/activation constant of Modifier i.
   */
  C_FLOAT64 getK(C_INT32 i);

  /**
   *  Retrieve the Hill coefficient of Modifier i.
   */
  C_FLOAT64 getn(C_INT32 i);

  /**
   *  Retrieve the number of negative modifiers
  *  @return C_INT32 the number of negative modifiers
   */
  C_INT32 getNegativeModifiers(void);

  /**
   *  Retrieve the number of positive modifiers
   *  @return C_INT32 the number of negative modifiers
   */
  C_INT32 getPositiveModifiers(void);

  /**
   *  Retrieve the number incoming links to this gene
   *  @return C_INT32 the in-degree
   */
  C_INT32 getInDegree();

  /**
   *  Increment the in-degree of this gene
   */
  void addInDegree();

  /**
   *  Retrieve the number outgoing links from this gene
   *  @return C_INT32 the out-degree
   */
  C_INT32 getOutDegree();

  /**
   *  Increment the out-degree of this gene
   */
  void addOutDegree();

  /**
   *  Decrement the in-degree of this gene
   */
  void decreaseInDegree();

  /**
   *  Decrement the out-degree of this gene
   */
  void decreaseOutDegree();

  /**
   *  Retrieve the total number of links (incoming and outgoing) of this gene
   *  @return C_INT32 the total degree
   */
  C_INT32 getTotalDegree();

  /**
   *  cleanup()
   */
  void cleanup();

  /**
   *  Sort the order of modifiers, activators at the top
   */
  void sortModifiers();
};

#endif // COPASI_CGene
