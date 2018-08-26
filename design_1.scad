$fn = 100;

union()
{
    difference()
    {
        cylinder(r = 23.8/2, h = 30);
        cylinder(r = 6/2, h = 30);
    }

    intersection()
    {
        cylinder(r = 23.8/2, h = 30);
        translate([0,4.1,20])
            {
                rotate([90,0,0])
                    {
                        cylinder(r = 10.81,h = 1.8);
                    }   
            }
    }   
}
