
$fn = 100;

union()
{
difference()
    {   translate([-36.7/2,-55,0])
    {
        cube([18.21,55,5]);
    }
    
        for(i = [0:5])
{
    rotate([0,0,60*i])
        {
            translate([31.5/2,0,0])
            {
                cylinder(r = 3/2, h = 10);
            }
        }
}
      
}
       
difference()
    {   cylinder(r = 37/2-0.2, h = 5);

    translate([0,6.9,0])
        {
            cylinder(r = 13/2, h = 5);
        }


for(i = [0:5])
{
    rotate([0,0,60*i])
        {
            translate([31.5/2,0,0])
            {
                cylinder(r = 3/2, h = 10);
            }
        }
}
}
}
