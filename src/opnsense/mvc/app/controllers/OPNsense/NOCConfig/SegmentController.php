<?php

/**
 *   Copyright (c) 2021-2022 Nova Intelligent Technology JSC.,
 *   Author: hai.nt <hai.nt@novaintechs.com>
 *   
 *   All rights reserved.
 *   
 *   --------------------------------------------------------------------------------------
 *   
 *   
 */

namespace OPNsense\NOCConfig;

/**
 * Class IndexController
 * @package OPNsense\NOCConfig
 */
class SegmentController extends \OPNsense\Base\IndexController
{
    public function indexAction()
    {
        $this->view->pick('OPNsense/NOCConfig/segment');
        $this->view->formSegment = $this->getForm("segment");
    }
}
