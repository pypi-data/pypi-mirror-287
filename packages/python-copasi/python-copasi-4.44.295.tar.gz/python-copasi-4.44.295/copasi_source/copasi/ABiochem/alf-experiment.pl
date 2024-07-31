#! /usr/bin/perl -w
#
# Virginia Bioinformatics Institute, Virginia Tech
# Biochemical Networks Modeling Group
# 
# This module written by Pedro Mendes, April 2003
#
# A-Biochem
#
# Alf-experiments.pl 
# This module processes all the Gepasi files,
# carrying out simulations of several experiments
#

use POSIX;

$pert = 0.5;
$tpred = 0.05;
$ttheo = 0.05;
if( $ARGV[0] =~ /^([+-]?)(?=\d|\.\d)\d*(\.\d*)?([Ee]([+-]?\d+))?$/ ) {$pert = $ARGV[0];}
if( $ARGV[1] =~ /^([+-]?)(?=\d|\.\d)\d*(\.\d*)?([Ee]([+-]?\d+))?$/ ) {$tpred = $ARGV[1];}
if( $ARGV[2] =~ /^([+-]?)(?=\d|\.\d)\d*(\.\d*)?([Ee]([+-]?\d+))?$/ ) {$ttheo = $ARGV[2];}

# All configuration parameters here

# file extension for graph files
$GEPASIEXTENSION = "gps";
# file extension for stats files
$STATEXTENSION = "netstat";
# gnuplot
#$GNUPLOT = "/usr/local/bin/gnuplot";
# Gepasi
$GEPASI = "/usr/local/bin/gepasi -r";
# graph layout program (force field)
$DOT = "/usr/local/bin/dot";
# alf's program
$RSA = "/usr/local/bin/rsa";

$counter = 0;

# processing
while( defined($statfile = <*.$STATEXTENSION>) )
{
	$counter++;
	$name = $statfile;
	$name =~ s/\.$STATEXTENSION//;
	# Gepasi filename
	$gfile = "$name.$GEPASIEXTENSION";
	print "$counter, $gfile ";

	# run Gepasi
	system "$GEPASI $gfile";

	open( STATFILE, "$statfile" );
	$vertex = 0;
	@stats = <STATFILE>;
	close(STATFILE);
    foreach $line (@stats) 
	{
      if ($line =~ /number of vertices\t([0-9]+)/)
	  {
	    $vertex = $1;
		if( $vertex>9) {$tick = $vertex/10;}
		else {$tick=1;}
	    last;
	  }
	}

    # get elasticity matrix from the txt file of the original
	for( $i=0; $i<$vertex*2; $i++ )
	{
	 for( $j=0; $j<$vertex; $j++ )
	 {
	  $elast[$i][$j] = 0.0;
	 }
	}
	$tfile = "$name.txt";
	open( TXTFILE, "$tfile" );
	while( defined($line = <TXTFILE> ))
	{
 	 while ($line =~ /e\(G([0-9]+) synthesis,\[G([0-9]+)\]\) =\s?((\+|-)?([0-9]+\.?[0-9]*|\.[0-9]+)([eE](\+|-)?[0-9]+)?)/g ) 
	 {
	  $i1 = ($1-1)*2;
	  $j1 = $2-1;
	  $e = $3;
	  $e =~ s/1\.7977e\+308/1\.797e\+308/;
	  $elast[$i1][$j1] = $e;
	 }
	 while ($line =~ /e\(G([0-9]+) degradation,\[G([0-9]+)\]\) =\s?((\+|-)?([0-9]+\.?[0-9]*|\.[0-9]+)([eE](\+|-)?[0-9]+)?)/g )
	 {
	  $i1 = ($1-1)*2+1;
	  $j1 = $2-1;
	  $e = $3;
	  $e =~ s/1\.7977e\+308/1\.797e\+308/;
	  $elast[$i1][$j1] = $e;
	 }
	}
	close( TXTFILE );
	$elastfile = "$name.ela";
	open( EFILE, ">$elastfile" );
	for( $i=0; $i<$vertex*2; $i++ )
	{
	 for( $j=0; $j<$vertex; $j++ )
	 {
	  print( EFILE "$elast[$i][$j]\t");
	 }
	 print( EFILE "\n");
	}
	close(EFILE);

    # read the original gepasi file and keep it all in memory
	open( GPSFILE, "$gfile" );
	@gpsfile = <GPSFILE>;
	close(GPSFILE);


    ########################################
    # HETEROZYGOUS STEADY STATE EXPERIMENT #
    ########################################
	$hssfile = $gfile;
	$hssfile =~ s/\.$GEPASIEXTENSION/\.hss\.$GEPASIEXTENSION/;
    # open the results file
	$resultsfile = $statfile;
	$resultsfile =~ s/\.$STATEXTENSION/\.hss.dat/;
	open( RESULTS, ">$resultsfile" );

    # one gene at a time, but start without changes
	for( $g=0; $g<=$vertex; $g++ )
	{
	  # write new files based on the original, with 
	  # $pert % different expression rate for each gene
	  open( HSSFILE, ">$hssfile" );
	  $r = 0; $t1 = 1;
      foreach $line (@gpsfile) 
	  {
	    if ($line =~ /^Report=1/) 
		{ 
		  print( HSSFILE "Report=0\n"); 
		  next;
		}
	    if ($line =~ /^ReportFile=(.+)\.([^.]*)\n/)
		{ 
		  print( HSSFILE "DynamicsFile=$1.hss.$2\n"); 
		  next; 
		}
	    if ($line =~ /^DynamicsFile=(.+)\.([^.]*)\n/)
		{ 
		  print( HSSFILE "DynamicsFile=$1.hss.$2\n"); 
		  next; 
		}
	    if ($line =~ /^SSFile=(.+)\.(.*)\n/) 
		{ 
		  $ssfile = "$1.hss.$2";
		  print( HSSFILE "SSFile=$ssfile\n");
		  next; 
		}
	    if ( ($t1==1) && ($line =~ /^Title=/) ) 
		{ 
		  print( HSSFILE "Title=$name heterozygous gene $g steady state experiment\n");
                  $t1=0;
		  next;
		}
        if ($line =~ /Equation= -> G([0-9]+)/)
	    {
		  # we're in the correct reaction
	      $r = $1;
	    }
		if( ( $r==$g ) && ( $line =~ /Param0=([-+]?[0-9]+[.]?[0-9]*([eE][-+]?[0-9]+)?)/ ) )
		{
		    # this is the basal rate of transcription
            $rate = $1 * $pert;
		    print( HSSFILE "Param0=$rate\n");
			# change $r so that we don't also change the degradation rate
			$r = 0;
		}
		else { print( HSSFILE $line ); }
	  }
	  close(HSSFILE);
	  # run Gepasi
	  system "$GEPASI $hssfile";
	  # and append the ss results to the result file
	  open( SSFILE, "$ssfile" );
	  while( <SSFILE> )
	  { print( RESULTS $_ ); }
	  close(SSFILE);
	  if( $g % ($tick) == 0 ) { print "."; } 
	}
    close(RESULTS);
	open( RESULTS, "$resultsfile" );
	$rrfile = "$resultsfile.xls";
	open( REDRESULTS, ">$rrfile" );
	# read first line
	$line = <RESULTS>;
	@wt = split(/\t/,$line);
	# calculate relative values, using first line
	for( $g=0; $g<$vertex; $g++ )
	{
	  $line = <RESULTS>;
	  @mt = split(/\t/, $line);
	  for( $i=0; $i<$vertex; $i++ )
	  {
	    if( $wt[$i]>1.0E-36 ) 
		{ 
		  $val = $mt[$i] / $wt[$i];
		}
		else { $val = 0.0; }
		if( $i!=0 ) { print( REDRESULTS "\t"); }
		print( REDRESULTS "$val");
	  }
	  print( REDRESULTS "\n" );
	}
    close(RESULTS);
    close(REDRESULTS);

	system "$RSA $name $vertex $tpred $ttheo";
	$pngfiled = "$name-rsa.png";
	$gfile = "$name.dot";
	if ($vertex < 500)
	 {system "$DOT -Tpng -o$pngfiled $gfile 2>>dot.log";}

    print "\n";
}
