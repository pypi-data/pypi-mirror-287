/**
 * This is an example on how to run an optimization task.
 * And how to access the result of an optimization.
 */

using System;
using org.COPASI;
using System.Diagnostics;

class example5 
{

   static void Main() 
   {
     Debug.Assert(CRootContainer.getRoot() != null);
     // create a new datamodel
     CDataModel dataModel = CRootContainer.addDatamodel();
     Debug.Assert(CRootContainer.getDatamodelList().size() == 1);
     // get the model from the datamodel
     CModel model = dataModel.getModel();
     Debug.Assert(model != null);
     model.setVolumeUnit(CUnit.fl);
     model.setTimeUnit(CUnit.s);
     model.setQuantityUnit(CUnit.fMol);
     CModelValue fixedModelValue=model.createModelValue("F");
     Debug.Assert(fixedModelValue != null);
     fixedModelValue.setStatus(CModelEntity.Status_FIXED);
     fixedModelValue.setInitialValue(3.0);   
     CModelValue variableModelValue=model.createModelValue("V");
     Debug.Assert(variableModelValue != null);
     variableModelValue.setStatus(CModelEntity.Status_ASSIGNMENT);
     // we create a very simple assignment that is easy on the optimization
     // a parabole with the minimum at x=6 should do just fine
     string s=fixedModelValue.getValueReference().getCN().getString();
     s="(<"+s+"> - 6.0)^2";
     variableModelValue.setExpression(s);
     // now we compile the model and tell COPASI which values have changed so
     // that COPASI can update the values that depend on those
     model.compileIfNecessary();
     ObjectStdVector changedObjects=new ObjectStdVector();
     changedObjects.Add(fixedModelValue.getInitialValueReference());
     changedObjects.Add(variableModelValue.getInitialValueReference());
     model.updateInitialValues(changedObjects);
     
     // now we set up the optimization

     // we want to do an optimization for the time course
     // so we have to set up the time course task first
     CTrajectoryTask timeCourseTask = (CTrajectoryTask)dataModel.getTask("Time-Course");
     Debug.Assert(timeCourseTask != null);
     // since for this example it really doesn't matter how long we run the time course 
     // we run for 1 second and calculate 10 steps
     // run a deterministic time course
     timeCourseTask.setMethodType(CTaskEnum.Method_deterministic);

     // pass a pointer of the model to the problem
     timeCourseTask.getProblem().setModel(dataModel.getModel());

     // get the problem for the task to set some parameters
     CTrajectoryProblem problem = (CTrajectoryProblem)timeCourseTask.getProblem();
     Debug.Assert(problem != null);

     // simulate 10 steps
     problem.setStepNumber(10);
     // start at time 0
     dataModel.getModel().setInitialTime(0.0);
     // simulate a duration of 1 time units
     problem.setDuration(1);
     // tell the problem to actually generate time series data
     problem.setTimeSeriesRequested(true);
    
     // get the optimization task
     COptTask optTask=(COptTask)dataModel.getTask("Optimization");
     Debug.Assert(optTask != null);
     // we want to use Levenberg-Marquardt as the optimization method
     optTask.setMethodType(CTaskEnum.Method_LevenbergMarquardt);
     
     // next we need to set subtask type on the problem
     COptProblem optProblem=(COptProblem)optTask.getProblem();
     Debug.Assert(optProblem != null);
     optProblem.setSubtaskType(CTaskEnum.Task_timeCourse);
     
     // we create the objective function
     // we want to minimize the value of the variable model value at the end of
     // the simulation
     // the objective function is normally minimized
     string objectiveFunction=variableModelValue.getObject(new CCommonName("Reference=Value")).getCN().getString();
     // we need to put the angled brackets around the common name of the object
     objectiveFunction="<"+objectiveFunction+">";
     // now we set the objective function in the problem
     optProblem.setObjectiveFunction(objectiveFunction);

     // now we create the optimization items
     // i.e. the model elements that have to be changed during the optimization
     // in order to get to the optimal solution
     COptItem optItem=optProblem.addOptItem(new CCommonName(fixedModelValue.getObject(new CCommonName("Reference=InitialValue")).getCN()));
     // we want to change the fixed model value from -100 to +100 with a start
     // value of 50
     optItem.setStartValue(50.0);
     optItem.setLowerBound(new CCommonName("-100"));
     optItem.setUpperBound(new CCommonName("100"));
     
     // now we set some parameters on the method
     // these parameters are specific to the method type we set above
     // (in this case Levenberg-Marquardt)
     COptMethod optMethod=(COptMethod)optTask.getMethod();
     Debug.Assert(optMethod != null);
     
     // now we set some method parameters for the optimization method
     // iteration limit
     CCopasiParameter parameter=optMethod.getParameter("Iteration Limit");
     Debug.Assert(parameter != null);
     parameter.setIntValue(2000);
     // tolerance
     parameter=optMethod.getParameter("Tolerance");
     Debug.Assert(parameter != null);
     parameter.setDblValue(1.0e-5);

     // create a report with the correct filename and all the species against
     // time.
     CReportDefinitionVector reports = dataModel.getReportDefinitionList();
     // create a new report definition object
     CReportDefinition report = reports.createReportDefinition("Report", "Output for optimization");
     // set the task type for the report definition to timecourse
     report.setTaskType(CTaskEnum.Task_optimization);
     // we don't want a table
     report.setIsTable(false);
     // the entries in the output should be seperated by a ", "
     report.setSeparator(new CCopasiReportSeparator(", "));

     // we need a handle to the header and the body
     // the header will display the ids of the metabolites and "time" for
     // the first column
     // the body will contain the actual timecourse data
     ReportItemVector header = report.getHeaderAddr();
     ReportItemVector body = report.getBodyAddr();
     
     // in the report header we write two strings and a separator
     header.Add(new CRegisteredCommonName(new CDataString("best value of objective function").getCN().getString()));
     header.Add(new CRegisteredCommonName(report.getSeparator().getCN().getString()));
     header.Add(new CRegisteredCommonName(new CDataString("initial value of F").getCN().getString()));
     // in the report body we write the best value of the objective function and
     // the initial value of the fixed parameter separated by a komma
     body.Add(new CRegisteredCommonName(optProblem.getObject(new CCommonName("Reference=Best Value")).getCN().getString()));
     body.Add(new CRegisteredCommonName(report.getSeparator().getCN().getString()));
     body.Add(new CRegisteredCommonName(fixedModelValue.getObject(new CCommonName("Reference=InitialValue")).getCN().getString()));

     
     // set the report for the task
     optTask.getReport().setReportDefinition(report);
     // set the output filename
     optTask.getReport().setTarget("example5.txt");
     // don't append output if the file exists, but overwrite the file
     optTask.getReport().setAppend(false);


     bool result=false;
     try
     {
       result=optTask.processWithOutputFlags(true, (int)CCopasiTask.ONLY_TIME_SERIES);
     }
     catch(System.ApplicationException e)
     {
         System.Console.Error.WriteLine("ERROR: "+e.Message);
		           String lastErrors =  optTask.getProcessError();
          // check if there are additional error messages
          if (!string.IsNullOrEmpty(lastErrors))
          {
              // print the messages in chronological order
              System.Console.Error.WriteLine(lastErrors);
          }

         System.Environment.Exit(1);
     }
     if(!result)
     {
         System.Console.Error.WriteLine("Running the optimization failed.");
		           String lastErrors =  optTask.getProcessError();
          // check if there are additional error messages
          if (!string.IsNullOrEmpty(lastErrors))
          {
              // print the messages in chronological order
              System.Console.Error.WriteLine(lastErrors);
          }

         System.Environment.Exit(1);
     }
     // now we check if the optimization actually got the correct result
     // the best value it should have is 0 and the best parameter value for
     // that result should be 6 for the initial value of the fixed parameter
     double bestValue=optProblem.getSolutionValue();
     Debug.Assert(System.Math.Abs(bestValue) < 1e-3);
     // we should only have one solution variable since we only have one
     // optimization item
     Debug.Assert(optProblem.getSolutionVariables().size() == 1);
     double solution=optProblem.getSolutionVariables().get(0);
     Debug.Assert(System.Math.Abs((solution-6.0)/6.0) < 1e-3);
  }

}
