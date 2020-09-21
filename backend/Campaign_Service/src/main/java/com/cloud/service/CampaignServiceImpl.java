package com.cloud.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.cloud.domain.CampaignDto;
import com.cloud.mapper.CampaignMapper;

@Service
public class CampaignServiceImpl implements CampaignService {

	@Autowired
	private CampaignMapper campaignMapper;

	@Override
	public List<CampaignDto> findAll(String campaignType, int pageNo, String type, String content) {
		type = type.trim();
		content = content.trim();
		return campaignMapper.findAll(campaignType, pageNo, type, content);
	}

	@Override
	public List<String> findTagByNo(int no) {
		return campaignMapper.findTagByNo(no);
	}

	@Override
	public CampaignDto findDetail(int no) {
		return campaignMapper.findDetail(no);
	}

	@Override
	@Transactional
	public int insertCampaign(CampaignDto dto) {
		int res = campaignMapper.insertCampaign(dto);
		int no = dto.getNo();
		System.out.println(no + "cccccccccccccccccccc");
		campaignMapper.insertTag(dto.getTag(), no);
		return res;
	}

	@Override
	public int updateCampaign(CampaignDto dto) {
		return campaignMapper.updateCampaign(dto);
	}

	@Override
	public int deleteCampaign(int no) {
		return campaignMapper.deleteCampaign(no);
	}

}
