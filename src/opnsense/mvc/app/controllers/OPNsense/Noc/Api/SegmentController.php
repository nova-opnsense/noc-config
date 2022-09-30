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

namespace OPNsense\Noc\Api;

use OPNsense\Base\ApiMutableModelControllerBase;

/**
 * a settings controller for our Noc app, uses our ApiMutableModelControllerBase type
 * @package OPNsense\Noc
 */
class SegmentController extends ApiMutableModelControllerBase
{
    protected static $internalModelName = 'segment';
    protected static $internalModelClass = 'OPNsense\Noc\Segment';

    public function searchItemAction()
    {
        return $this->searchBase("segments.segment", array('enabled','hubId','name','lastUpdate','status'), "name");
    }

    public function setItemAction($uuid)
    {
        return $this->setBase("segment", "segments.segment", $uuid);
    }

    public function addItemAction()
    {
        return $this->addBase("segment", "segments.segment");
    }

    public function getItemAction($uuid = null)
    {
        return $this->getBase("segment", "segments.segment", $uuid);
    }

    public function delItemAction($uuid)
    {
        return $this->delBase("segments.segment", $uuid);
    }

    public function toggleItemAction($uuid, $enabled = null)
    {
        return $this->toggleBase("segments.segment", $uuid, $enabled);
    }
}
